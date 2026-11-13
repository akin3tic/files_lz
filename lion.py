import csv

import matplotlib.pyplot as plt
from docx import Document

#работа с текстом и словами
doc = Document("lion.docx")
ft = " ".join([p.text for p in doc.paragraphs]).lower() #full text
w = ft.split() #words
uw = list(set(w)) #unique words
cuw = [] #count of unique words
cw = 0 #count of word

#подсчет для слов
for i in range(len(uw)):
     for i2 in range(len(w)):
          if uw[i] == w[i2]:
               cw += 1
     cuw.append(cw)
     cw = 0

#таблица
with open("text.csv","w",newline="",encoding="utf-8-sig") as file:
     writer = csv.writer(file, delimiter=";")
     writer.writerow(["Слово", "Частота встречи, раз" , "Частота встречи в %"])

     #вывод данных слов в таблицу
     for i3 in range(len(uw)):
          writer.writerow([uw[i3], cuw[i3] , round((cuw[i3]/len(w))*100, 2)])

#работа с буквами
a = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я" #alphabet
l = a.split()
cl = [] #list for count of letter
c = 0 #count of letter

#подсчет букв
lt = [p for word in w for p in word]
for i4 in range(len(l)):
     for i5 in range(len(lt)):
          if l[i4] == lt[i5]:
               c += 1
     cl.append(c)
     c = 0

#вывод гистограммы встречаемости букв
plt.bar(l, cl, color='blue', edgecolor='black')
plt.show()