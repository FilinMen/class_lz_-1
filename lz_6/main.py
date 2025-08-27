# Имрот необходимых модулей и библиотек
from multi_threading import Multithreading
from multi_processing import Multiprocessing
from asyncc import Asynchron
import asyncio


# Функция main
def main():
    user_input=input('Какой алгоритм вы хотите использовать:\n'
    '1 — Многопоточность\n'
    '2 — Многопроцессорность\n' 
    '3 — Асинхрон\n')
    if user_input == '1':
        process = Multithreading()
        process.making_threads()
    elif user_input == '2':
        data = list(range(1, 501))
        process = Multiprocessing(20)
        process.results_of_comparison(data)
    elif user_input == '3':
        process = Asynchron()
        asyncio.run(process.handler())
    
    
if __name__ == '__main__':
    main()