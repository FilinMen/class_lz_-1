# (Вариант 5) 
# Задание 2. Синхронизация процессов с помощью Lock.
# Несколько процессов записывают в один файл без конфликтов.
# Записывать можно любое количество случайных символов.
# Количество процессов делать не более 10.

# Импорт необходимых библиотек
import multiprocessing
import time
import random
import string

# Создание  функции для генерации случайных символов в одну строку
def multiproc(lock, my_file, num_chars):
    #  Процесс записи случайных чисел
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_chars))
    with lock: 
        with open(my_file, "a") as f:
            f.write(random_chars )
            
# Определяем количество создаваемых 
# процессов (10 по условию), а также количество случайных символов (100)
def record (my_file="parent_file.txt", the_proces=10, quantity__chars=100):
    lock = multiprocessing.Lock() 
    # Создание списка для занесения результата и команда для начала отсчета текущего времени 
    my_list = []
    start = time.time()
    
    for _ in range(the_proces):
        the_proces = multiprocessing.Process(target=multiproc, args=(lock, my_file, quantity__chars))
        the_proces.start()
        my_list.append(the_proces)

    for p in my_list:
        p.join()
    # Расчет и вывод затраченного времени
    delta= time.time() - start
    print(f"Время синхронизации: {delta} ")

if __name__ == "__main__":
    record()