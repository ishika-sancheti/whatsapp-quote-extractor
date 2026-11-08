from src import parser, matcher, exporter

def main():
    messages=parser.parse_messages()
    latest_quotes=matcher.matching(messages)
    exporter.export_csv(latest_quotes)

if __name__=="__main__":
    main()