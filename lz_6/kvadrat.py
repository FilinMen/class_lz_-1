from concurrent.futures import ThreadPoolExecutor
import time


def kvadrat(x):  
    return x * x
 
numbers = range(10001)

start_time = time.time()
results = [kvadrat(x) for x in numbers]
end_time = time.time()
no_threads_time = end_time - start_time

start_time = time.time()
with ThreadPoolExecutor(max_workers=10) as pool:
    results_t = list(pool.map(kvadrat, numbers))
end_time = time.time()
threads_time = time.time() - start_time
 
print(results)
print(f"Время выполнения с потоками: {threads_time} секунд🫅")
print(f"Время выполнения без потоков: {no_threads_time} секунд🥺")