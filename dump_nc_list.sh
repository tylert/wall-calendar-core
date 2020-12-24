#!/usr/bin/env bash

# Generate the TXT file
python radio_events_LNLARES.py > list.txt

# Generate the CSV file from the TXT file
cat <(echo "Date,Controller") <(cat list.txt) | tr ' ' ',' > list.csv

# Generate the spreadsheet files from the CSV file
libreoffice --headless --convert-to ods list.csv
libreoffice --headless --convert-to xlsx list.csv

# Generate the word processor files from the TXT file
libreoffice --headless --convert-to odt list.txt
libreoffice --headless --convert-to docx list.txt

# Generate the PDF file from the TXT file
libreoffice --headless --convert-to pdf list.txt
