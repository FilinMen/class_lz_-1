from stata import Statistika


file_path = r"E:\praktika\class_lz_-1\class_lz_-1\lz_3\personal_transactions.csv" 
stats = Statistika(file_path)
print(stats.load_data())
print(stats.plot_pie_chart())