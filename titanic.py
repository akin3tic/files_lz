import matplotlib.pyplot as plt
import pandas as pd

#переводим файл в формат csv и сохраняем в исходную папку
titanic = pd.read_parquet("titanic.parquet")
titanic.to_csv("output.csv", index=False, encoding="utf-8")
text_csv = pd.read_csv("output.csv")
#загружаем таблицу из CSV
df = pd.read_csv("output.csv")
#считаем проценты для каждого класса распределяем числа от 0 до 1 по строкам
table = pd.crosstab(df["Pclass"], df["Survived"], normalize="index") * 100
#меняем столбцы местами, чтобы сначала шел 1 (Выжил), а затем 0 (Не выжил)
table = table[[1, 0]]
#задаем понятные названия для подписей на графике
classes = ["1-й класс", "2-й класс", "3-й класс"]
survived = table[1]  #процент выживших
died = table[0]  #процент погибших
#cоздаем холст для рисования
fig, ax = plt.subplots(figsize=(8, 5))
#рисуем столбцы друг на друге
ax.bar(classes, survived, width=0.5, label="Выжил", color="#001D62")
ax.bar(classes, died, width=0.5, bottom=survived, label='Не выжил', color="#BA5E20", )
#внешний вид
ax.set_title('Соотношение выживших по классам (%)', fontsize=14)
ax.set_ylabel('Проценты')
ax.set_ylim(0, 100)  #ограничиваем ось Y строго до 100%
ax.legend()
plt.show()