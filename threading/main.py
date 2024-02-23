import time
import threading
import requests


def do_something(index):
    print('Process Started!')
    url = 'https://picsum.photos/200/300'
    response = requests.get(url)
    with open(f'images/image_{index}.png', 'wb') as file:
        file.write(response.content)
    print('Process Ended!')


t1 = time.time()

arr = []

for i in range(5000):
    th1 = threading.Thread(target= do_something, args=[i])
    th1.start()
    arr.append(th1)

for thread in arr:
    thread.join()

t2 = time.time()

print(t2 - t1)