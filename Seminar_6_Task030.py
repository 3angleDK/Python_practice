# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


lst = []
a1 = float(input("Введите 1-й элемент прогрессии: "))
d = float(input("Введите шаг прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))
for i in range(n):
    lst.append(a1 + i * d)

print(lst)