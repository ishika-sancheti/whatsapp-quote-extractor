#identify requests and supplier replies for the same and match them
from parser import parse_messages
import re

pattern1=re.compile(                                                                #customer side
    r"(quote|pl\.?\s*quote|please\s+quote|"
    r"price\s*&\s*availability|price\s+and\s+availability|"
    r"please\s+confirm\s+price|kindly\s+check|"
    r"please\s+confirm|kindly\s+quote|"
    r"please\s+arrange\s+quotation|"
    r"any\s+alternative)", re.IGNORECASE)   
pattern2=re.compile(r"\b\d[\d,]*(?:\.\d{1,2})?\s*\+\s*\d+%", re.IGNORECASE)             #supplier side

status_pattern=re.compile(r"\b(no stock|not available|available|ready|wait)\b",re.IGNORECASE)           #other than price, if they share status updates

attachment_pattern=re.compile(r"(image omitted|document omitted|WhatsApp Image|\.jpeg|\.jpg|\.png)", re.IGNORECASE)        #should def be ignore

quantity_pattern=re.compile("\b\d+\s*(?:nos?\.?|pieces?|pcs?)\b", re.IGNORECASE)

def matching(messages):
    quotations=[]
    #first categorise the messages as req or resp
    for msg in messages:
        if msg["message"] is None:
            continue
        if attachment_pattern.search(msg["message"]):
            continue
        if msg["sender"]=="Ganesh Enterprises":
            if pattern1.search(msg["message"]):
                category="request"
            else: 
                category="detail"
        else:
            if pattern2.search(msg["message"]) or status_pattern.search(msg["message"]):
                category="response"
            else: continue   
        quotations.append({**msg, "category": category})

    #for matching req w responses 
    active_req=None
    active_quote_index=None
    matched=[]
    pending_responses=[]

    for item in quotations:
        if item["category"]=="request":
            active_req=item                             #this req is now active 
            active_quote_index=None                     #no quote received yet so index is none
        elif item["category"]==["detail"]:
            if active_req is not None and active_quote_index is None:
                active_req["message"]+= " " + item["message"]          
        elif item["category"]=="response":
            if active_req is None:                      #if no req found 
                pending_responses.append(item)          
                continue
            if active_quote_index is None:              #if no quote received, then match the active req w the response
                matched.append({
                    "item-details":active_req["message"],
                    "price":item["message"],
                    "request-date":active_req["timestamp"],
                    "quote-date":item["timestamp"]
                })
                active_quote_index=len(matched)-1       
            else:
                matched[active_quote_index]["price"]=item["message"]
                matched[active_quote_index]["quote-date"]=item["timestamp"]
    
    #last quote wins
    latest_quotes={}
    for quote in matched:
        item_key=quantity_pattern.sub("", quote["item-details"])
        item_key=quote["item-details"].strip(" -,.").lower()
        latest_quotes[item_key]=quote                       #rewrite if same appears again
        
    #participants=set(msg["sender"] for msg in messages)
    #supplier=participants - {"Ganesh Enterprises"}
    print("CLASSIFIED:", quotations)
    print("MATCHED:", len(matched), matched)
    print("UNMATCHED:", len(pending_responses), pending_responses)

messages=parse_messages()
result=matching(messages)
