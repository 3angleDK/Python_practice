# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import sqrt
n = int(input("Введите сумму 2x чисел: "))
m = int(input("Введите произведение 2x чисел: "))
d = n * n - 4 * m
x = int((n + sqrt(d)) / 2)
y = n - x
print(f"Загаданные числа {x} и {y}.")
