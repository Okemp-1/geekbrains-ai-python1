'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''



my_file = open('test_2.txt', 'r',  encoding='utf-8')
'''открываем файл'''
content = my_file.read()
'''читаем содержимое'''
print(f'Содержимое файла: \n\n{content}\n')
'''выводим его'''
my_file = open('test_2.txt', 'r',  encoding='utf-8')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
'''считаем количество строк читая их построчно'''
my_file = open('test_2.txt', 'r',  encoding='utf-8')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
    '''считаем каждый символ каждой строки'''
my_file = open('test_2.txt', 'r',  encoding='utf-8')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
'''считаем количество всех слов, разделённых пробелом'''
my_file.close()
'''закрываем файлик'''