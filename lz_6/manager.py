import multiprocessing
import time

def fill_dict(gen_dict, proc_id):
    for i in range(5):
        gen_dict[proc_id * 10 + i] = f"value_{i}"
        time.sleep(0.5)

def manager():
    with multiprocessing.Manager() as manager:
        gen_dict = manager.dict()
        processes = []

        for i in range(3):
            p = multiprocessing.Process(target=fill_dict, args=(gen_dict, i))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print("Общий словарь:", dict(gen_dict))
