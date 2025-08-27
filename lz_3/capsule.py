from log import log
import matplotlib.pyplot as plt
import pandas as pd


class Diagramma:
    
    def __init__(self, cards):
        self.cards = cards 
        
    @log
    def diag(self):

        df = pd.read_csv(self.cards)

        count = df.iloc[:, 5].value_counts()#Выписываем все строки из 6 столбца и 
        label = count.index
        size = count.values
        colors = ['lightgreen', 'lightblue', 'silver']
        plt.pie(size, labels = label, colors = colors, autopct = '%1.1f%%', startangle = 90) #создаём круговую диаграмму
        plt.axis('equal')
        plt.show()

    def __del__(self):
        print(" ")