'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''


from sys import argv
#для работы скрипта с параметрами необходимо в терминале/консоли
#выбрать директорию с файлом GeekBrains_AI_Strzhelinsky_Python_4-1 например, '(venv) macbook-air:lesson_4 admin$'
#и ввести 'python GeekBrains_AI_strzhelinsky_Python_4-1.py 240 100 5000'

name, time, salary, bonus = argv

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Заработная плата сотрудника {res} рублей')
except ValueError:
    print('Один из параметров time, salary или bonus не является целочисленным значением')
