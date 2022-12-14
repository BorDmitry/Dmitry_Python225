import json


def add_decor(func):
    def wrap(*args, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = {}
        func(*args, filename)
        print("Файл сохранён")
    return wrap


class Paises:
    def __init__(self, pais, capital):
        self.pais = pais
        self.capital = capital
        data[self.pais] = self.capital

    def __str__(self):
        return f'{self.pais}: {self.capital}'

    @ classmethod
    @ add_decor
    def add_country(cls, new_pais, new_capital, filename):
        data[new_pais] = new_capital

        with open(filename, 'w') as f:
            data[new_pais] = new_capital
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    @add_decor
    def remove_country(self, del_country, filename):
        if del_country in data:
            del data[del_country]

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет.")

    @classmethod
    @add_decor
    def search_data(cls, pais, filename):
        if pais in data:
            print(f"Страна {pais} есть в базе."
                  f" Её столица - {data[pais]}.")
        else:
            print(f"Страны {pais} нет в базе.")


    @classmethod
    @add_decor
    def cheng_capital(cls, pais, new_capital, filename):
        if pais in data:
            data[pais] = new_capital

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print(f"Страны {pais} нет в базе.")

    @ classmethod
    def info_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


data = {"Россия": "Москва"}
filename1 = 'list_of_countries.json'
with open(filename1, 'w') as f_save:
   json.dump(data, f_save, indent=2, ensure_ascii=False)


n = 0
while 0 <= n <= 6:
    print("*" * 40)
    print('Выбор действия:\n'
          '1 - добавление данных\n'
          '2 - удаление данных\n'
          '3 - поиск данных\n'
          '4 - редактирование данных\n'
          '5 - просмотр данных\n'
          '6 - завершение работы\n')

    n = int(input('Ввод: '))
    if n == 1:
        new_pais = input("Введите название страны (с заглавной буквы): ")
        new_capital = input("Введите название столицы страны (с заглавной буквы): ")
        Paises.add_country(new_pais, new_capital, filename='list_of_countries.json')
        print(f"Страна {new_pais} добавлена")
    elif n == 2:
        name = input("Введите имя страны (с заглавной буквы) для удаления: ")
        Paises.remove_country(name, filename='list_of_countries.json')

    elif n == 3:
        name = input("Введите название (с заглавной буквы) страны для поиска: ")
        Paises.search_data(name, filename='list_of_countries.json')

    elif n == 4:
        name = input("Введите название страны (с заглавной буквы) для редактирования: ")
        new_value = input("Введите новое название столицы (с заглавной буквы): ")
        Paises.cheng_capital(name, new_value, filename='list_of_countries.json')
    elif n == 5:
        Paises.info_from_file(filename='list_of_countries.json')
    elif n == 6:
        print("Программа завершена")
        break

# ВЫВОД:

# C:\Users\Dmitry\Scripts\HomeWork\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/HomeWork/D_Z_Countries_Decor.py
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 1
# Введите название страны (с заглавной буквы): Франция
# Введите название столицы страны (с заглавной буквы): Paris
# Файл сохранён
# Страна Франция добавлена
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 4
# Введите название страны (с заглавной буквы) для редактирования: Франция
# Введите новое название столицы (с заглавной буквы): Париж
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва', 'Франция': 'Париж'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 1
# Введите название страны (с заглавной буквы): Голландия
# Введите название столицы страны (с заглавной буквы): Амстердам
# Файл сохранён
# Страна Голландия добавлена
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 2
# Введите имя страны (с заглавной буквы) для удаления: Голландия
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва', 'Франция': 'Париж'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 1
# Введите название страны (с заглавной буквы): Испания
# Введите название столицы страны (с заглавной буквы): Мадрид
# Файл сохранён
# Страна Испания добавлена
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 3
# Введите название (с заглавной буквы) страны для поиска: Россия
# Страна Россия есть в базе. Её столица - Москва.
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва', 'Франция': 'Париж', 'Испания': 'Мадрид'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 6
# Программа завершена
#
# Process finished with exit code 0
