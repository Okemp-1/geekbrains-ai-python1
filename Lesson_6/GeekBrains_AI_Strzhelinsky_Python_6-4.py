'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

'''class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def go(self):
        print('{} is stoping!'.format(self.name))

    def go(self, direction):
        print('{} is turning to'.format(self.name, direction))

    def show_speed(self):
        print('Current speed', self.speed)

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed is more then max!')

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > 40:
            return ('Speed is more then max!')
class PoliceCar(Car):
    pass'''


#Нашёл крутое решение. Но там сначала срабатывает рандом, а потом уже экземпляры. Поэтому они все поворачивают в одну сторону всегда
import random

direction_options = ['налево', 'направо']

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} движется')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction=random.choice(direction_options)):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысил скорость! Максимальная разрешённая для этого класса автомобилей скорость - 60 км/ч')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, color, name, speed=220, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(
                f'{self.name} превысил скорость! Максимальная разрешённая для этого класса автомобилей скорость - 40 км/ч')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

print('-' * 50)

# test TownCar class
print('Town car: ')
town_car_example = TownCar(35, 'белый', 'KIA Rio')
print(f'Цвет {town_car_example.name} - {town_car_example.color}')
town_car_example.go()
town_car_example.turn()
town_car_example.show_speed()
town_car_example.speed = 50
print(f'{town_car_example.name} разгоняется до {town_car_example.speed} км/ч!')
town_car_example.show_speed()
town_car_example.speed = 70
print(f'{town_car_example.name} разгоняется до {town_car_example.speed} км/ч!')
town_car_example.show_speed()
town_car_example.stop()
if town_car_example.is_police == True:
    print('Это полицейский автомобиль')
else:
    print('Это не полицейский автомобиль')
print('-' * 50)

# test SportCar class
print('Sport car: ')
sport_car_example = SportCar('желтый', 'Lamborgini Galardo')
print(f'Цвет {sport_car_example.name} - {sport_car_example.color}')
sport_car_example.go()
sport_car_example.turn()
sport_car_example.show_speed()
sport_car_example.stop()
print('-' * 50)

# test WorkCar class
print('Work car: ')
work_car_example = WorkCar(25, 'серый', 'ГАЗ 3221 Газель')
print(f'Цвет {work_car_example.name} - {work_car_example.color}')
work_car_example.go()
work_car_example.turn()
work_car_example.show_speed()
work_car_example.speed = 50
print(f'{work_car_example.name} разгоняется до {work_car_example.speed} км/ч!')
work_car_example.show_speed()
work_car_example.stop()
print('-' * 50)

# test PoliceCar class
print('Police car: ')
police_car_example = PoliceCar(60, 'бело-синий', 'Ford Mondeo')
print(f'Цвет {police_car_example.name} - {police_car_example.color}')
police_car_example.go()
police_car_example.turn()
police_car_example.show_speed()
police_car_example.speed = 80
print(f'{police_car_example.name} разгоняется до {police_car_example.speed} км/ч!')
police_car_example.show_speed()
#print(police_car_example.is_police)
police_car_example.stop()
if police_car_example.is_police == True:
    print('Это полицейский автомобиль')
else:
    print('Это не полицейский автомобиль')
print('-' * 50)