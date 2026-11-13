import csv
import re
import matplotlib.pyplot as plt
from docx import Document

#работа с текстом и словами
doc = Document("lion.docx")
ft = " ".join([p.text for p in doc.paragraphs]).lower() #full text
w = re.findall(r"[а-яё]+", ft)

#подсчет для слов
wc = {} #words count
for i in w:
    wc[i] = wc.get(i, 0) + 1

#таблица
with open("text.csv","w",newline="",encoding="utf-8-sig") as file:
     writer = csv.writer(file, delimiter=";")
     writer.writerow(["Слово", "Частота встречи, раз" , "Частота встречи в %"])

     #вывод данных слов в таблицу
     for i2 in wc:
          writer.writerow([i2, wc[i2], round((wc[i2] / len(w)) * 100, 2)])

#работа с буквами
a = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я" #alphabet
l = a.split()

#подсчет букв 
cl = [ft.count(letter) for letter in l]

#вывод гистограммы встречаемости букв
plt.bar(l, cl, color='blue', edgecolor='black')
plt.show()