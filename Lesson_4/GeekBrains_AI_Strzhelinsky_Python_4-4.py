'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]

1 рабочий вариант
source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in source_list if source_list.count(i) == 1]
print(new_list)

вариант с вводом чисел'''
source_list = list(map(int, input('Введите через пробел числа, например 2 2 2 7 23 1 44 44 3 2 10 7 4 11 : >>> ').split()))
new_list = [x for x in source_list if source_list.count(x) == 1]
print('Не имеющие повторов числа из вашего списка: ')
print(' '.join(map(str, new_list)))
