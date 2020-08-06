'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''

#через re не работает с 0 и float, но зато своё исключение
#и пропускает отрицательные и всякие интересные числа
#а isdigit, isnumeric и isdecimal ни одно с отрицательными не работает
#ещё остались варианты с делением на 1 - лень было пробовать
# и длинная цепочка из
# try:
#     int(a)
# except ValueError:
#     try:
#         float(a)
#     except ValueError:
#         print "This is not a number"
#         a=0
# if a==0:
#     a=0
# else:
#     print a
# в общем, это не та задача, на которую надо было полтора часа убивать)

import re

class NotANumberException(Exception):
    def __init__(self, txt):
        self.txt = txt

result_list = []
while True:
    value = input('Введите целое положительное число для добавления в список или stop для выхода: ')

    if value == 'stop':
        print(f'Список на момент выхода {result_list}.')
        break

    if value == 0:
        result_list.append(int(value))

    try:
        num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
        isnumber = re.match(num_format, value)
        if isnumber:
        # if not value.isnumeric():
        #     raise NotANumberException('NaN!')
            result_list.append(int(value))
            print(f'Значение добавлено в список {result_list}.')
        else:
            raise NotANumberException('NaN!')
    except NotANumberException as error:
        print('Вы ввели не число, попробуйте снова или введите stop для выхода.')

'''
#один хрен с дробными не работает
#class NotANumberException(Exception):
#    def __init__(self, txt):
#        self.txt = txt

result_list = []
while True:
    value = input('Введите ЛЮБОЕ число для добавления в список или stop для выхода: ')

    try:
        float(value)
        result_list.append(int(value))
        print(f'Значение добавлено в список {result_list}.')
    except ValueError:
    #except NotANumberException as error:
        print('Вы ввели не число, попробуйте снова или введите stop для выхода.')
'''
