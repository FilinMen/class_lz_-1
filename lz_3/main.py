from graf_static import GraphStats



file_path = r"C:\Users\Asus\Desktop\new practic\class_lz_-1\lz_3\playstation_players.csv"  # Путь к файлу с данными
stats = GraphStats(file_path)
print(stats.load_data())
print(stats.plot_pie_chart())