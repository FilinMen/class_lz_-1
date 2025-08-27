import pandas as pd

class Money:
    def __init__(self, input_file):
        self.data = pd.read_csv(input_file)

    def __invert__(self):
        initial_count = len(self.data)
        self.data = self.data.drop_duplicates()
        removed_count = initial_count - len(self.data)
        print(f"Дубликаты удалены. Удалено записей: {removed_count}")

    def split_and_save(self, column_name, file_true, file_false):
        subset_nol = self.data[self.data[column_name] == 0.0]
        subset_ne_nol = self.data[self.data[column_name] != 0.0]

        subset_nol.to_csv(file_true, index=False)
        subset_ne_nol.to_csv(file_false, index=False)
        print(f"Данные сохранены: {file_true}, {file_false}")













