import os,pdfplumber
import pandas as pd

file = os.path.expanduser("1.pdf")

with pdfplumber.open(file) as pdf:
    for i in range(0,len(pdf.pages)):
        first_page = pdf.pages[i]

        text = first_page.extract_text()
        with open('1.txt', 'a') as f:

            f.write(text)
    # print(table)
