import pandas as pd


class File:

    def __init__(self):

        self.data = pd.read_csv('var7.csv')

    
    def __pos__(self):# удаляем дубликаты 
        
        df = pd.read_csv('var7.csv')
        self.data_clear = df.drop_duplicates()
        self.data_clear.to_csv('del_dub.csv', index=False) 

    def dup(self):

        print(f'колличество дубликатов: {len(self.data) - len(self.data_clear)}')
    
    def sort(self, file_name):

        data = pd.read_csv(file_name)

        data['Дата оплаты'] = pd.to_datetime(data['Дата оплаты'], format = '%d-%m-%Y')
        data_after = data.loc[data['Дата оплаты'] >= '2014-01-01']
        data_after.to_csv('after_2014.csv', index = False) 

        data['Дата оплаты'] = pd.to_datetime(data['Дата оплаты'], format = '%d-%m-%Y')
        data_before = data.loc[data['Дата оплаты'] < '01-01-2014']
        data_before.to_csv('before_2014.csv', index = False) 
    

    def __del__(self):
        print('del')
    
def main():
    
    dates = File()
    +dates
    dates.dup()
    dates.sort('del_dub.csv')


if __name__ == "__main__":
    main()