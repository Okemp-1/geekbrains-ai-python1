'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_list = []
while True:
    line = input("Введите любые символы для записи для создания новой строки в файле: >>> ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w",  encoding='utf-8') as file_obj:
        file_obj.writelines(my_list)