# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def getMin(lst):
    m = lst[0]
    for i in lst:
        if i < m:
            m = i
    return m

def getMax(lst):
    m = lst[0]
    for i in lst:
        if i > m:
            m = i
    return m

lst = [1,3,3,3,4]

min = getMin(lst)
max = getMax(lst)

print(f"Исходные оценки: {lst}")
for i in range(0,len(lst)):
    if lst[i] == max:
        lst[i] = min
print(f"Результат: {lst}")
