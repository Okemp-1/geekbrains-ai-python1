'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного
кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_metod(self):
        return f"Чтобы покрыть дорогу {self._length} на {self._width} метров нужно {self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т асфальта."

road_1 = Road(5000, 20)
print(road_1.calculation_metod())