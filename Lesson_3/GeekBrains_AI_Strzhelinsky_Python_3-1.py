'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return 'Нельзя делить на 0, мир сломается!'
    except ValueError:
        return 'Нужно вводить число'
print('Сейчас вы введёте 2 числа: X и Y, а программа разделит X на Y')
print(f'X / Y = {my_func(int(input("Enter x = ")), int(input("Enter y = ")))}')
# Я ещё в round() это всё заворачивал, но тогда крашится round и ZeroDivisionError не отрабатывает
# Чтобы работало, надо преобразовать в int в ветке try