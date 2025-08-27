import pandas as pd
import matplotlib.pyplot as plt
from log import log_decorator

class Statistika:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
    
    @log_decorator()
    def load_data(self):
        self.df = pd.read_csv(self.file_path)
    
    @log_decorator()
    def plot_pie_chart(self):
        if self.df is None:
            raise ValueError("Данные не загружены. Используйте load_data().")
        expense_data = self.df.groupby('Account Name')['Amount'].sum()
        
        plt.figure(figsize=(7, 7))
        expense_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title("Траты по типу платежной системы")
        plt.ylabel("")  
        plt.show()

file_path = r"E:\praktika\class_lz_-1\class_lz_-1\lz_3\personal_transactions.csv"   
stats = Statistika(file_path)
