# WhatsApp Quote Extractor

A Python-based tool that extracts quotation requests and supplier responses from exported WhatsApp chat files and generates a structured CSV containing item details and their corresponding prices or availability statuses.

## Features

- Parses exported WhatsApp `.txt` chat files.
- Identifies quotation requests sent by the customer.
- Extracts item descriptions from subsequent customer messages.
- Identifies supplier responses containing prices or availability updates.
- Matches customer requests with supplier responses.
- Retains the latest quotation when the same item is quoted multiple times.
- Ignores image and document attachment messages.
- Exports the extracted quotations into a CSV file.

## Project Structure

```text
whatsapp-quote-extractor/
│
├── data/
│   └── input/             # WhatsApp chat export files
│
├── output/                # Generated CSV files
│
├── src/
│   ├── __init__.py
│   ├── parser.py           # Parses WhatsApp chat messages
│   ├── matcher.py          # Classifies and matches requests and responses
│   ├── exporter.py         # Exports matched quotations to CSV
│
├── main.py                 # Application entry point
└── README.md
```

## Usage

1. Export the WhatsApp conversation using the **Export Chat** option in WhatsApp.
2. Save the exported `.txt` file in the `data/input/` directory.
3. Run the application from the project root:

```bash
python main.py
```

4. The extracted quotations will be saved as a CSV file in the `output/` directory.

## Output

The generated CSV contains two columns:

| Item | Price |
|---|---|
| ABCD40TR, 10 nos | 1230+18% |
| AB-123, 1 nos | Not available |
| Accumulator, 7 nos | 5/7 days wait |

The `Price` column can contain either a quoted price or an availability status, depending on the supplier's response.
