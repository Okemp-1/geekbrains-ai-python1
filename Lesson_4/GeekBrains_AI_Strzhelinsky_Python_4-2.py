'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

'''numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#result_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
#result_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(f'Исходный список {numers}')
print(f'Новый список {result_list}')
Эта реализация возвращает 300'''

numbers = list(map(int, input('Введите числа через пробел, например 300 2 12 44 1 1 4 10 7 1 78 123 55: >>> ').split()))
result_list = [val for idx, val in enumerate(numbers) if idx > 0 and numbers[idx - 1] < val]
print('Элементы списка, значения которых больше предыдущего')
print(' '.join(map(str, result_list)))