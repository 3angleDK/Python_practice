# Найти из двух чисел большее
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(f"Число a = {a} больше числа b = {b}.")
elif a == b:
    print("Числа a и b равны.")
else:
    print(f"Число b = {b} больше числа a = {a}.")
