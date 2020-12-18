import random

n = int(input('Введи количество бочек: '))
spisok = []

for i in range(1, n + 1): # Заполнение списка
    spisok.append(i)

for i in range(len(spisok)): # Цикл для вывода
    d = random.choice(spisok) # Выбираем случайным образом элемент из списка
    spisok.remove(d) # Удаление элемента
    print(d) # Вывод элемента
