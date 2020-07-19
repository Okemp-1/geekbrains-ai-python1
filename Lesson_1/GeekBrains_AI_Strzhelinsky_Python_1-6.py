'''
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

print('Вы спортсмен и занимаетесь ежедневными пробежками? Наша методика позволяет каждый день увеличивать ваш результат на 10%!')
print('Укажите дистанцию вашего последнего забега, а мы подскажем, сколько дней вам надо заниматься по нашей программе, чтобы достигнуть желаемого результата')
a = int(input("Сколько километров вы пробежали в последний раз? >>> "))
print('Мы уже считаем этот день первым, тренировка началась!')
b = int(input("Сколько километров вы хотите пробегать? >>> "))
day = 1
while a < b:
    a = a + 0.1 * a
    day += 1
    print(f'На {day:.0f} день вы пробежите {a:.2f} км')
print(f'По нашей методике вы достигнете требуемых показателей на {day:.0f} день')