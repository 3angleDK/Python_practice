# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

n = int(input("Введите номер билета: "))
m1 = n % 10 + (n // 10) % 10 + (n // 100) % 10
m2 = (n // 1000) % 10 + (n // 10000) % 10 + n // 100000
if m1 == m2:
    print(f"Билет {n} счастливый.")
else:
    print(f"Билет {n} не счастливый.")
