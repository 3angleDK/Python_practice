# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if a == 0 and b == 0:
        return 0
    if b == 0:
        return 1 + sum(a - 1, 0)
    else:
        return sum(a , 0) + sum(b , 0)
    
print(sum(2,10))
