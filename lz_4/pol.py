import pandas as pd

class Frame:
    def __init__(self, input_file):
        self.data = pd.read_csv(input_file)

    def __invert__(self):
        initial_count = len(self.data)
        self.data = self.data.drop_duplicates()
        removed_count = initial_count - len(self.data)
        print(f"Dublicates have been delete. Number of deleted: {removed_count}")

    def split_and_save(self, column_name, file_true, file_false):
        subset_true = self.data[self.data[column_name] == "да"]
        subset_false = self.data[self.data[column_name] == "нет"]

        subset_true.to_csv(file_true, index=False)
        subset_false.to_csv(file_false, index=False)
        print(f"Data saved: {file_true}, {file_false}")













