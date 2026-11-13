import csv
from docx import Document
import matplotlib as mt
doc = Document("lion.docx")#
ft = " ".join([p.text for p in doc.paragraphs]).lower()#full text
w = ft.split()#words
with open("text.csv","w",newline="",encoding="UTF-8") as file:
     writer = csv.writer(file, delimiter=";")
     writer.writerow(["Слово", "Частота встречи, раз" , "Частота встречи в %"])
     writer.writerow([word1, c1 , ""])
     writer.writerow([word2, c2 , ""])