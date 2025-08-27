import multiprocessing
import random

def square(number):

    return number ** 2

def born():

    return [random.randint(-1_000_000, 1_000_000) for i in range(1000)]

def numbers():

    num = born()  
    process_num = 2

    with multiprocessing.Pool(processes=process_num) as pool:
        squar = pool.map(square, num)  

    print("Квадраты чисел:", squar) 


