import threading
import time

def worker(event, thread_id):
    print(f"Поток {thread_id} ждёт сигнал")
    event.wait()
    print(f"Поток {thread_id} начал работу")

def event(num_threads=10):
    start_event = threading.Event()
    threads = []

    for i in range(min(num_threads, 10)):
        t = threading.Thread(target=worker, args=(start_event, i))
        threads.append(t)
        t.start()

    time.sleep(2)
    print("Работать")
    start_event.set()

    for t in threads:
        t.join()
