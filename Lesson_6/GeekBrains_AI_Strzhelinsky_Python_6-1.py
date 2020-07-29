'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

#нашёл, как затирать прошлый результат print'а и заодно цвет на ANSI colors
import time
import itertools

class TrafficLight:
    __color = [["красный", [7, 31]], ["жёлтый", [2, 33]], ["зелёный", [5, 32]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[1m", end="")
            time.sleep(light[1][0])

start = TrafficLight()
start.running()

'''
#эт первое решение
from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Красный', 7), ('Жёлтый', 2), ('Зелёный', 5))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color.format(sec))
            sleep(sec)

traffic_light = TrafficLight()
traffic_light.running()'''