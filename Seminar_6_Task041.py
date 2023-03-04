# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5 
# 1 2 3 4 5 
# Вывод: 
# 0

# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

# lst = []
# n = int(input("Введите количество элементов в массиве: "))
# for i in range(n):
#     lst.append(int(input(f"Введите {i+1} элемент массива: ")))

lst = [1, 2, 3, 4, 5]
count = 0
for i in range(1, len(lst)-1):
    if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
        count += 1
print(count)

lst = [1, 5, 3, 5, 4]
count = 0
for i in range(1, len(lst)-1):
    if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
        count += 1
print(count)
