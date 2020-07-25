'''
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import re

def calculate_hours(calc_line: str):
    line_of_hours = re.sub(r'\D', ' ', calc_line)
    total_hours = 0
    for hour in line_of_hours.split():
        total_hours += float(hour)
    return total_hours

overall_subject_info = {}
with open('text_6.txt', 'r', encoding='utf-8') as file_read:
    for line in file_read.readlines():
        listed_line = line.split(': ')
        overall_subject_info[listed_line[0]] = calculate_hours(listed_line[1])

print(f'Общее количество часов: >>> \n{overall_subject_info}')