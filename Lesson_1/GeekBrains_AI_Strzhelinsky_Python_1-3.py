'''
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
'''

n = int(input('Введите любое целое число, а программа посчитает сумму n+nn+nnn: >>> ')),
n = int("%s" % n)
nn = int("%s%s" % (n,n))
nnn = int("%s%s%s" % (n,n,n))
summ = n + nn + nnn
print (f'{n} + {nn} + {nnn} = {summ}')