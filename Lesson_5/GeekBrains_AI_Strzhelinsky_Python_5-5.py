'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

def summary():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел: >>> \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(f'Сумма введёных чисел равна {sum(map(int, my_numb))}')
    except IOError:
        print('Ошибка ввода-вывода')
    except ValueError:
        print('Неправильное значение, введите число')
summary()