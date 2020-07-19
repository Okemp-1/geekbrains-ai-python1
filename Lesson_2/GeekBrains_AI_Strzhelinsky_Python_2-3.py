'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите номер месяца: >>> "))
if month == 1 or month == 12:
    print(f'Согласно реализации программы через dict, {month}-ый месяц это {seasons_dict.get(1)}.')
    print(f'А через список, это — {seasons_list[0]}. Конечно, они одинаковые.')
if month == 2:
    print(f'Согласно реализации программы через dict, {month}-ой месяц это {seasons_dict.get(1)}.')
    print(f'А через список, это — {seasons_list[0]}. Конечно, они одинаковые.')
elif month == 4 or month ==5:
    print(f'Согласно реализации программы через dict, {month}-ый месяц это {seasons_dict.get(2)}.')
    print(f'А через список, это — {seasons_list[1]}. Конечно, они одинаковые.')
if month == 3:
    print(f'Согласно реализации программы через dict, {month}-ий месяц это {seasons_dict.get(2)}.')
    print(f'А через список, это — {seasons_list[1]}. Конечно, они одинаковые.')
elif month == 6 or month == 7 or month == 8:
    print(f'Согласно реализации программы через dict, {month}-ой месяц это {seasons_dict.get(3)}.')
    print(f'А через список, это — {seasons_list[2]}. Конечно, они одинаковые.')
elif month == 9 or month == 10 or month == 11:
    print(f'Согласно реализации программы через dict, {month}-ый месяц это {seasons_dict.get(4)}.')
    print(f'А через список, это — {seasons_list[3]}. Конечно, они одинаковые.')
else:
    print("Такого месяца не существует.")