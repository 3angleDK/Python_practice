# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Введите количество долек шоколадки в ширину: "))
m = int(input("Введите количество долек шоколадки в длину: "))
k = int(input("Введите сколько долек отломить: "))

if k % m == 0 or k % n == 0:
    print("YES")
else:
    print("NO")