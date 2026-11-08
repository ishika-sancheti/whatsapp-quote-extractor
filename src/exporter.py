import csv

def export_csv(latest_quotes):
    headings=["Item", "Price"]

    with open(r"C:\Users\Ishika\whatsapp-quote-extractor\output\output.csv", 'w', newline="", encoding="utf-8") as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=headings)
        writer.writeheader()

        for key, value in latest_quotes.items():
            writer.writerow({
                "Item":value["item-details"],
                "Price":value["price"]
            })
