from log import log
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Circle:

    def __init__(self, file):
        self.file = file

    @log
    def img(self):

        df = pd.read_csv(self.file)
        col = df.iloc[:, 5].value_counts() #все строки из шестого столбца
        label = col.index
        size = col.values
        colors = ['red','gray','green']
        plt.pie(size, labels = label, colors = colors, autopct = '%1.1f%%') #создает круговую диаграмму
        plt.axis('equal')
        plt.show()

    def __del__(self):
        print("")

def main(): 

    start = Circle('personal_transactions.csv')
    start.img()

if __name__ == "__main__":
    main()
