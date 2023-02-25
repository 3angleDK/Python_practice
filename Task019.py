# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

lst = [1, 2, 3, 4, 5]
k = int(input("Введите величину сдвига: "))
k %= len(lst) # на случай ввода отрицательных и слишком больших k
res =[]
for i in range(0, len(lst)-k):
    res.append(lst[i + k])
for i in range(0, k):
    res.append(lst[i])
print(f"Исходный список: {lst}")
print(f"Результат: {res}")

print(f"Результат: {[lst[(i + k) % (len(lst))] for i in range(len(lst))]}")
print(f"Результат: {lst[k:] + lst[:k]}")
 