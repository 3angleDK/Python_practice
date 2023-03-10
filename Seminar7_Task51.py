# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by(f, vlaues):
#     tmp = f(values[0])
#     res = True
#     for x in values:
#         res = res and tmp == f(x)
#     return res

def same_by(f, values):
    return len(set(f(x) for x in values)) <= 1

values = [0, 2, 10, 6] 
# values = [1, 3, 11, 7] 

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')