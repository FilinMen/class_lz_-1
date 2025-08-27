import pandas as pd
import matplotlib.pyplot as plt
from log import log_decorator

class GraphStats:
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
        
        expense_data = self.df.groupby('country')['playerid'].sum()
        
        plt.figure(figsize=(7, 7))
        expense_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title("Количество игроков PS")
        plt.ylabel("")
        plt.show()

file_path = r"C:\Users\Asus\Desktop\new practic\class_lz_-1\lz_3\playstation_players.csv"
stats = GraphStats(file_path)
