import threading
import time


class Multithreading:
    
    def __init__(self):
        self.threads = []
    
    def callback(self):
        for i in range(1, 51):
            time.sleep(2)
    
    def monitor(self):
        for i in range(1, 51):
            print(f'{i}/50')
            time.sleep(2)
    
    def making_threads(self):

        print('Запущенно:')

        thread = threading.Thread(target=self.callback)
        thread.start()
        self.threads.append(thread)
        
        thread_progress = threading.Thread(target=self.monitor)
        thread_progress.start()
        self.threads.append(thread_progress)
        
        for t in self.threads:
            t.join()
        
        print("Завершено.")
    

if __name__ == "__main__":
    process = Multithreading()
    process.making_threads()