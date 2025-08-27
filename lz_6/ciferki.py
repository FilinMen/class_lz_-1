from concurrent.futures import ThreadPoolExecutor

import multiprocessing
import time


def ciferki(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    numbers = range(10001)
    start_time = time.time()
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(ciferki, numbers)
    end_time = time.time()
    process_time = time.time() - start_time


    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(ciferki, numbers))
    end_time = time.time()
    threads_time = time.time() - start_time

    print(f"Время выполнения с потоками: {process_time} сек")
    print(f"Время выполнения без потоков: {threads_time} сек")
