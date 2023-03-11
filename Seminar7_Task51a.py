# Написать функцию, которая принимает список строк и возвращает список строк,
# содержащих только одноо слово, с использованием лямбда-функцииЖ
# strings = ["Hello, world!", "This is a sentence.", "Another sentence"]
# ["Hello,", "sentence.", "Anoter"]

lst = ["Hello, world!", "This is a sentence.", "Another sentence", "One", "Two"]

res = list(filter(lambda x: len(x.split(" ")) == 1, lst))
print(res)

