try:
    with open("GeekBrains_AI_Strzhelinsky_Python_8-4.py, "r", encoding='utf-8'") as f_obj:
        f_obj.read()
except OSError as error:
    print('Пожалуйста, откройте файл GeekBrains_AI_Strzhelinsky_Python_8-4.py')