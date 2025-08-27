# (Вариант 5) 
# Задание 1. Параллельная запись в файлы
# Создать 10 потоков, которые генерируют и записывают
# 100 случайных чисел в отдельные файлы с использованием
# потоков и без них, сравнить показатели по времени и
# вывести в консоль понятные сообщения. 

# Импорт необходимых библиотек
import threading # Импорт модуля, необходимого для создания и управления потоками выполнения.
import time # Импорт модуля для работы со временем
import random # Импорт модуля для генерации псевдослучайных чисел

# Функция, создающая файл и записывающая туда 100 случайных чисел
def threaded_recording(the_new_file):
    # Открытие файла для записи, превращение чисел в строку для записи
    with open(the_new_file, "w") as f:
        numbers = [str(random.randint(1, 100)) for _ in range(100)]
        # Запись чисел
        f.write(" ".join(numbers))

# Однопоточная запись
start = time.time()
for i in range(10):
    threaded_recording(f"single_threaded_recording{i+1}.txt")
# Расчет затраченного времени
single_threaded_time = time.time() - start


# Многопоточная запись
start = time.time()
threads = []
for i in range(10):
    # Само создание одного потока
    thread = threading.Thread(target=threaded_recording, args=(f"multi_threaded_recording{i+1}.txt",))
    # Расчет затраченного времени
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

multi_threaded_time = time.time() - start

# Вывод сраывнения времени
print(f"Сравнение времени выполнения для однопоточной и многопоточной записи:")
print(f"Однопоточный режим: {single_threaded_time}")
print(f"Многопоточный режим: {multi_threaded_time}")