# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

lst = []

n = int(input("Введите количество элементов массива: "))
for i in range(0, n):
    lst.append(int(input(f"введите {i+1}-й элемент массива: ")))
k = int(input("Введите искомый элемент массива: "))

count = 0
for i in lst:
    if i == k:
        count += 1
print(f"Элемент {k} встречается в массиве {count} раз(а).")