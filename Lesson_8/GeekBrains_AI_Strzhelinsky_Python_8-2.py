'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivZero(Exception):
    def __init__(self, errordescription):
        self.errordescription = errordescription

def division(divider, denominator):
    if denominator == 0:
        raise DivZero('Деление на 0 невозможно. Пока...')
    else:
        division_result = divider / denominator
        print('При делении {0} на {1} получилось {2}'.format(divider, denominator, division_result))
    return divider / denominator

try:
    num_1 = int(input('Введите числитель: >>> '))
    num_2 = int(input('Введите знаменатель: >>> '))
    division(num_1, num_2)
except DivZero as errordescription:
    print('{0}'.format(errordescription))