"""1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран."""

var_1 = 10
var_2 = 5
var_3 = 3

print("У нас есть несколько целочисленных переменных: var_1, var_2 и var_3"),
print("Они принимают значения 10, 5 и 3 соответственно, значит, можно написать команду type(var_1): "),
print(type(var_1), ", ", type(var_2), ", ", type(var_3)),

print("Вы можете сами задать любые значения переменных, попробуйте"),

var_1 = float(input("Введите значение первой переменной, например, дробное число: >>> ")),
'''Добавим проверочку
while(var_1 != float)
    print('Ну чего ты, не можешь ввести циферку, поставить точку и ввести ещё циферку?')
Чего-то не разобрался я, как это сделать :('''
var_2 = input("Для второй переменной введите значение другого типа, например, текст: >>> "),
var_3 = int(input('Ну и давайте введём обычный int-type: >>> ')),

print('Отлично! А теперь посмотрим, какие типы переменных у нас стали')

print(f'А вот и наши значения — var_1: {var_1} var_2: {var_2} и var_3: {var_3}'),