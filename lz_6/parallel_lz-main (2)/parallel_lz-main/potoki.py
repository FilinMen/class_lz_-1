import requests # библиотека для HTTP-запросов
import time
import threading

def load(url, results):

    response = requests.get(url, verify=False)
    results.append(f"{url}: {len(response.content)} байт загружено")

urls=[
    "https://www.similarweb.com",
    "https://twitch.tv",
    "https://google.com",
    "https://rutube.ru",
    "https://youtube.com",
    "https://ya.ru",
    "https://wikipedia.org",
    "https://ozon.ru",
    "https://whatsapp.com/"
    "https://avito.ru", 
]

def no_threa():
  
  start = time.time()

  done = [] 

  for url in urls:
      load(url,done)

  end = time.time()
  print(f"Без потоковое:")

  for result in done:
      print(result)
  print(f"Потрачено времен:{end - start}")
  return end - start

def threa():

    start = time.time()

    threads = []
    done = []

    for url in urls:

        thread = threading.Thread(target = load, args=(url, done))
        threads.append(thread)
        thread.start()

    for thread in threads:

        thread.join()

    end = time.time()
    print("Потоковое:")

    for result in done:

        print(result)
    print(f"Затрачено времени: {end - start:} секунд")
    return end - start

