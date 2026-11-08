#for identifying messages
import re

def parse_messages():
    file_path=r"C:\Users\Ishika\whatsapp-quote-extractor\data\input\supplier_chat.txt"
    pattern=re.compile(
        r'^\[(?P<timestamp>[^\]]+)\]\s+'
        r'(?P<sender>[^:]+):\s?'
        r'(?P<message>.*)$', re.MULTILINE)
    
    with open(file_path, "r", encoding="utf-8") as new_file:
        content=new_file.read()
        result=pattern.finditer(content)
        result_list=[]
        for item in result:
            result_list.append(item.groupdict())
    return result_list




