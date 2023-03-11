# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# data = [["Саврасков", "Мерин", "Коновалович", "8-909-909-9111"]]
data = []
filename = 'file.txt'

def InputData(recnum):
    lastname = input("Введите фамилию: ")
    firstname = input("Введите имя: ")
    middleame = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    if recnum >= len(data):
        data.append([lastname, firstname, middleame, phone])
    else:
        data[recnum] = [lastname, firstname, middleame, phone]

def OutputData(start, end):
    for i in range(start, end):
        print(f"{i+1}. " + "\t".join(data[i]))

def LoadData():
    try:
        with open(filename, 'r') as fin:
            for line in fin:
                data.append(list(line.strip().split(", ")))
    except FileNotFoundError:
        return
    print("Файл успешно загружен.")


def SaveData():
    with open(filename, 'w') as fout:
        for rec in data:
            fout.write(", ".join(rec) + "\n")
    print("Файл успешно сохранен.")

def FindData():
    searchstr = input("Введите искомую запись: ")
    flag = False
    for i in range(len(data)):
        for item in data[i]:
            if item.upper().find(searchstr.upper()) >= 0:
                if not flag:
                    flag = True
                    print("Найденные записи:")
                OutputData(i, i+1)
                break

    if not flag:
        print("Записи с такими параметрами не найдены!")

def DeleteData():
    numrec = int(input("Введите номер удаляемой записи: "))
    if numrec <= len(data):
        data.pop(numrec - 1)
    else:
        print("Записи с таким номером не существует.")

def ChangeData():
    numrec = int(input("Введите номер изменяемой записи: "))
    if numrec <= len(data):
        InputData(numrec - 1)
    else:
        print("Записи с таким номером не существует.")

LoadData()
while True:
    print("Список команд:")
    print("  i - ввести данные;")
    print("  o - вывести данные;")
    print("  c - изменить данные;")
    print("  s - сохранить данные в в файл;")
    print("  f - найти данные;")
    print("  d - удалить данные;")
    print("  q - выйти из программы.)")
    cmd = input("Введите команду: ")
    if cmd == "i":
        InputData(len(data))
    elif cmd == "o":
        OutputData(0, len(data))
    elif cmd == "c":
        ChangeData()
    elif cmd == "s":
        SaveData()
    elif cmd == "f":
        FindData()
    elif cmd == "d":
        DeleteData()
    elif cmd == "q":
        break
    else:
        print("Неверная команда!!!")
