'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income_dict['wage']
        self._income_bonus = income_dict['bonus']

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return income_dict['wage'] + income_dict['bonus']

income_dict = {'wage': 100000, 'bonus': 30000}

test_worker_1 = Position('Александр', 'Старолат', 'CEO mottor')

print(f'{test_worker_1.get_full_name()}, {test_worker_1.position}, доход с учётом премии: {test_worker_1.get_total_income()}')
