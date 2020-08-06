'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

import re
#чтобы через match формат проверять

class MyDate():
    def __init__(self, datestr):
        dd, mm, yyyy = self.formatstring(datestr)
        if MyDate.ddmmyyycorrect(dd, mm, yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

    def __str__(self):
        return "%02d-%02d-%04d" % (self.dd, self.mm, self.yyyy)

    @classmethod
    def formatstring(cls, datestr):
        match = re.match(r'(\d{2})-(\d{2})-(\d{4})', datestr)
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            raise ValueError("Заданная дата " + datestr + " не соответствует формату DD-MM-YYYY")

    @staticmethod
    def ddmmyyycorrect(dd, mm, yyyy):
        if not(yyyy >= 0 and yyyy <= 2999):
            raise ValueError( "Некорректный год — число должно быть в диапазоне от 0001 до 2999, а задано: " + str(yyyy))
        if not(mm >= 1 and mm <= 12):
            raise ValueError("Некорректный месяц - число должно быть в диапазоне от 01 до 12, а задано: " + str(mm))
        if not(dd >= 1 and dd <= 31):
            raise ValueError("Некорректный день - число должно быть в диапазоне от 01 до 31, а задано: " + str(dd))
        return True

#Пошли тесткейсы
print('пробуем сегодняшнюю дату в верном формате')
try:
    d = MyDate('04-08-2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем сегодняшнюю дату в неверном формате')
try:
    d = MyDate('4.08.2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем сегодняшнюю дату в неверном формате')
try:
    d = MyDate('4/08/2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем сегодняшнюю дату в неверном формате')
try:
    d = MyDate('4/VII 2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем сегодняшнюю дату в неверном формате')
try:
    d = MyDate('4 августа 2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем 35-04-2020 - ошибка даты - число')
try:
    d = MyDate('35-04-2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем 04-13-2020 - ошибка даты - месяц')
try:
    d = MyDate('04-13-2020')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)

print('пробуем 04-08-3540 - ошибка даты - год')
try:
    d = MyDate('04-08-3540')
    print(d)
except Exception as err:
    print(err)
print('-' * 50)
