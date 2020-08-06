'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

'''
5. Продолжить работу над первым заданием. #видимо, четвёртым))
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
'''

'''6. Продолжить работу над вторым заданием. #видимо, пятым))
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''

### СКЛАД ###
class Warehouse:

    __technics = dict()
    __removed_technics = dict()

### ПРИЁМ ТОВАРА ###
    def add_Technic(self, key, value):
        if self.__technics.get(key) == None:
            self.__technics[key] = 0
        self.__technics[key] += value

### ВЫДАЧА ТОВАРА ###
    def remove_Technic(self, key, value):
        rest = self.__technics.get(key)
        if rest != None and rest >= value:
            self.__technics[key] -= value
            if self.__technics[key] == 0:
                del self.__technics[key]

    def num(self, key):
        value = self.__technics.get(key)
        return value if value != None else 0

    def technics_in_warehouse(self):
        #if models == 0:
            print('*****\nСкладской остаток:\n*****')
            for i in self.__technics:
                print(f'{models[i].model} - {self.num(i)} шт.')
            print('*****\n')
        #else:
        #   print('Склад пуст')


    def removed_technics(self):
        print(f'\nПередано в офис:\n{self.__technics}')

### ОРГТЕХНИКА ###
class Orgtechnik:

    def __init__(self, model, price, dpi, paper_format):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_format = paper_format

    @property
    def model(self):
        return self._model

### ПРИНТЕР ###
class Printer(Orgtechnik):

    def __init__(self, model, price, dpi, paper_format, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_format)

### СКАННЕР ###
class Scanner(Orgtechnik):
    pass

### КОПИР ###
class Copier(Orgtechnik):

    def __init__(self, model, price, dpi, paper_format, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_format)


### ЭКЗЕМПЛЯРЫ ОРГТЕХНИКИ (МОДЕЛИ) ###
models = [Printer('Принтер HP Deskjet 3845', 6835, '4800x1200', 'A4', 'inkjet'),
          Printer('Принтер Canon i-SENSYS LBP112', 9890, '4800x1200', 'A4', 'laserjet'),
          Copier('МФУ XEROX WorkCentre 6515DN', 42620, '600x600', 'A3', 28, 50000),
          Scanner('Сканер EPSON Perfection V370 Photo', 5600, '4800×9600', 'A4')]

warehouse = Warehouse()
warehouse.technics_in_warehouse()

### МЕНЮ ###
### ПРИЁМ / СПИСАНИЕ ###
while True:
    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')
    if action in ['1', '2']:

### СПИСОК ОРГТЕХНИКИ ###
        s = ''
        for i, eq in enumerate(models):
            s += f'\n<{i}> {eq.model} ({warehouse.num(i)} шт.)'
### ВЫБОР МОДЕЛИ И КОЛИЧЕСТВА ###
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}\n')
### МОДЕЛЬ ###
            try:
                model = int(input('модель > '))
                if model in range(len(models)):
### КОЛИЧЕСТВО ###
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Ошибка ввода. Введите число от <0> до <{len(models)}>.') #не могу понять, откуда он берёт <4>, когда список пуст
                continue
            else:
### ОБРАБОТКА СОБЫТИЙ ####
                print('\nОперация:')
### ПРИЁМ НА СКЛАД ###
                if (action == '1'):
                    print(f'Принято на склад {models[model].model} - {n} шт.\n\n')
                    warehouse.add_Technic(model, n)
### СПИСАНИЕ СО СКЛАДА ###
                elif (action == '2'):
                    max = warehouse.num(model)
### ПРОВЕРКА ВЫДАЧА < НАЛИЧИЕ ###
                    if (n > max):
                        n = max
                        print(f'Операция отменена. На складе {n} шт. {models[model].model} - этого недостаточно!')
                    print(f'Выдано со склада {models[model].model} - {n} шт.')
                    warehouse.remove_Technic(model, n)

### ПОКАЗАТЬ СКЛАДСКОЙ ОСТАТОК ###
                warehouse.technics_in_warehouse()
                break

        if (input('\n Нажмите <Enter> чтобы продолжить или любую другую клавищу для выхода...') != ''):
                break
### EXIT ###
    elif action == '':
        break
    else:
        print('Ошибка ввода. Для выбора введите <1> или <2>.')