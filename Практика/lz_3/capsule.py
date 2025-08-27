# (Вариант 3) Необходимо написать класс, который будет
# обрабатывать полученный датафрейм, и выводить на
# экран статистику в виде круговой диаграммы (количество игроков PS).

# Иморт необходимых библиотек 
import pandas as pd
import matplotlib.pyplot as plt
import getpass
from datetime import date, datetime
import os

# Создание декоратора
def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        
        user_name = getpass.getuser()
        func_name = func.__name__
        formatted_date = date.today().strftime("%d-%m-%Y")
        formatted_time = datetime.now().time()

        if os.path.isfile("logs.csv"):
            print("Файл существует")
            file_df = pd.read_csv("logs.csv")
            df = pd.DataFrame([len(file_df),user_name, func_name,formatted_date, formatted_time],
            columns=['id','user_name', 'func_name', 'formatted_date', 'data_time'])
            df.to_csv('logs.csv', mode='a', index=False)

        else:
            print("Файл не существует")
            df = pd.DataFrame([0 ,user_name, func_name,formatted_date, formatted_time],
            columns=['id','user_name', 'func_name', 'formatted_date', 'data_time'])
            df.to_csv('logs.csv')


        return original_result
    return wrapper

# Создание класса  для обработки DataFrame и построения
# диаграммы на основание обработанной информации
class Processing():
    def __init__(self):
        pass


    @log # Употребление декоратора 

    # Функция, обрабатывающая DataFrame и создающащая диаграмму
    def processing(self):
        # Считка данных и расчет уникалдьных значений
        df = pd.read_csv('playstation_players.csv')
        country_name = df['country'].value_counts()

        # Построение диаграммы
        plt.figure(figsize=(10,7))
        plt.pie(country_name, labels=country_name.index, autopct = '%1.1f%%', startangle = 140)
        plt.title('Количество игроков PS')
        plt.axis('equal')
        plt.show()

# Создание функции main()
def main():
    proc = Processing()
    proc.processing()

if __name__=="__main__":
     main()