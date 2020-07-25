'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json

try:
    with open('text_7.txt', 'r') as f:
        company_info = {}
        for line in f:
            name_company, form, profit, cost = line.split()
            try:
                profit = int(profit)
                cost = int(cost)
            except ValueError:
                print('В файле должны быть числа')
            else:
                proceeds = profit - cost
                company_info[name_company] = proceeds
    print(f'Словарь компаний и их прибылей (убытков): {company_info}')
    profit_making_firm = [value for value in company_info.values() if value > 0]
    average_profit = {"average_profit": round(sum(profit_making_firm) / len(profit_making_firm), 2)}
    print(f'Словарь со средней прибылью: {average_profit}')
    data_for_file = [company_info, average_profit]
    with open("text_77.json", "w") as write_f:
        json.dump(data_for_file, write_f, ensure_ascii=False, sort_keys=True, indent=2)
        '''https://pyneng.readthedocs.io/ru/latest/book/17_serialization/2_json.html - здесь нашёл, как структуру в JSON сохранить'''
except IOError:
    print('Ошибка ввода-вывода')