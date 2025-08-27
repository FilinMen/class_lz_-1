# var5 - настоящий файл
# var4 - пустой файл
# var3 - неверный файл (структура)

# Импорт необходимых библиотек
import pandas as pd
from pandas.errors import EmptyDataError
# Выводл расшифровки значений возможных ошибок для пользователя
print('Значения ошибок:')
print('er1: Файл не обнаружен')
print('er2: Файл пустой')
print('er3: Содержимое файла не совпадает с оригиналом')
print('er4: Расщирение не соответствует формату файла')


# Создание класса, обрабвтывающего файл
class Payment:

    def __init__(self):
        pass
    
    # Создание метода для проверки наличия файла
    def processing1(self):
        try:
            with open('var5.csv', 'r') as file:
                print(file.read())
        except FileNotFoundError as er1:
            print("Возникла следующая ошибка:{er1}")
        
        else:
            print('Файл обработан')
    
    # Создание метода для проверки файла на наличие содержимого
    def processing2(self):
        try:
            with open('var5','r') as file:
                pd.read_csv(file)
        except EmptyDataError as er2:
            print('Возникла следующая ошибка:{er2}')
        else:
            print('Файл обработан')


    # Создание файла, который сравнит полученный датасет с оригиналом(Проверка названий столбцов)
    def processing3(self):
        # Читаем файлы и заносим названия столбцов в список
        orig = pd.read_csv('var5.csv')
        my_file = pd.read_csv('var3.csv')
        column_names_list_orig = orig.columns.tolist()
        column_names_list = my_file.columns.tolist()
        # Сравниваем списки
        if column_names_list_orig==column_names_list:
            print('Проверка на er3. Названия столбцов совпадают')

        try:
            column_names_list_orig==column_names_list
        except ValueError as er3:
            print('Возникла следующая ошибка:{er3}'
            ' Ожидалось:{column_names_list_orig}. Сравниваемый:{column_names_list}')
        else:
            print('Файл обработан')

    # Создание файла, который сравнит полученный датасет с оригиналом(Проверка типов данных столбцов)
    def processing4(self):
            orig = pd.read_csv('var5.csv')
            my_file = pd.read_csv('file')
            orig_types = orig.dtypes
            my_file_types = my_file.dtypes
            # Сравниваем типы данных
            if orig_types == my_file_types:
                print('Проверка на er3. Типы данных столбцов совпадают')
            
            try:
                orig_types == my_file_types
            except ValueError as er3:
                print('Возникла следующая ошибка:{er3}'
                ' Ожидалось:{orig_types}. Сравниваемый:{my_file_types}')
            else:
                print('Файл обработан')

    # Проверка расширения файла
    def proceessing5(self):
        try:
            pd.read_csv('file')
        except ValueError as er4:
            print('Возникла следующая ошибка:{er4}')
        else:
            print('Файл обработан')

    # Создание функции main()
    def main():
        
        payment = Payment()
        payment.processing1
        payment.processing2
        payment.processing3
        payment.processing4

    if __name__ == "__main__":
        main()