'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}i'

complex_number_1 = ComplexNumber(2, -1)
complex_number_2 = ComplexNumber(-1, 5)
print(f'Комплексное число 1:\n{complex_number_1.a} + {complex_number_1.b}i')
print(f'Комплексное число 2:\n{complex_number_2.a} + {complex_number_2.b}i')
print('-----' * 20)
print(f'Результат сложения:\n{complex_number_1 + complex_number_2}')
print(f'Результат умножения:\n{complex_number_1 * complex_number_2}')