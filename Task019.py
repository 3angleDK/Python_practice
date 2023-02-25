# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
k = int(input("Введите величину сдвига: "))
k %= len(list) # на случай ввода отрицательных и слишком больших k
res =[]
for i in range(0, len(list)-k):
    res.append(list[i + k])
for i in range(0, k):
    res.append(list[i])
print(f"Исходный список: {list}")
print(f"Результат: {res}")

print(f"Результат: {[list[(i + k) % (len(list))] for i in range(len(list))]}")
