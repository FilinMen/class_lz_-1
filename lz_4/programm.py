# Импорт используемых библиотек
import pandas as pd


# Создание класса
class Text:
    def __init__(self, data : pd.DataFrame):
        self.data = data

   
    def dub(self): # Подсчет количества дубликатов и удаление их

        count = self.data.duplicated().sum()
        print(f'Количество повторяющихся строк в наборе данных: {count}')
    
    def __invert__(self):
        df_unique = self.data.drop_duplicates()
        return df_unique.to_csv('var1_only.csv')
    
    
    def divide(self):# разделяет датафрейм
        df_fiz = self.data[self.data["Участники гражданского оборота"] == "физ. лицо"]
        df_yur = self.data[self.data["Участники гражданского оборота"] == "юр. лицо"]

        df_fiz.to_csv("first.csv", index=False)
        df_yur.to_csv("second.csv", index=False)

# Функция main
def main():

    df = Text(pd.read_csv('var1.csv'))
    df.dub()
    df.divide()
    ~df
    


if __name__ == "__main__":
    main()