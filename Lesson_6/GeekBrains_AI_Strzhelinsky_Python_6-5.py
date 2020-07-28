'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen_example = Pen('ручкой')
pen_example.draw()

pencil_example = Pencil('карандашом')
pencil_example.draw()

handle_example = Handle('маркером')
handle_example.draw()