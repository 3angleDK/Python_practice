# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# from math import abs

lst = []

n = int(input("Введите количество элементов массива: "))
for i in range(0, n):
    lst.append(int(input(f"введите {i+1}-й элемент массива: ")))
x = int(input("Введите искомый элемент массива: "))

y = lst[0]
for i in lst:
    if abs(x - i) < abs(x - y):
        y = i
print(f"Ближайший к {x} элемент в массиве = {y}.")