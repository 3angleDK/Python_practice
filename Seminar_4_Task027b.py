# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – 
# соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите 
# программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1: ОРРОРОРООРРРО
# Sample Output 1: 3

# Sample Input 2: ООООООРРРОРОРРРРРРР
# Sample Output 2: 7
# Sample Input 3: ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3: 31

st = "ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР"
lst = st.split("О")
print(len(max(lst, key=len)))

# t=0
# while "Р"*(t+1) in s:
#     t+=1
# print(t)


# count = 0
# for s in lst:
#     if len(s) > count:
#         count = len(s)
# print(count)
