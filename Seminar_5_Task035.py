# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def IsNumberPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, 20):
    if IsNumberPrime(i):
        print(f"Число {i} простое.")
    else:
        print(f"Число {i} составное.")
