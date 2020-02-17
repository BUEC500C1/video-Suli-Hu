import queue
import threading
import numpy as np
import time
import os

class VideoCompressor():

    def __init__ (self, pool_size = 3, queue_size = 10):
        self.pool_size = pool_size
        self.queue_size = queue_size

    def execute(self, filename):
        t = threading.Thread(target = self.compress, args = (filename,) )
        return t

    def compress(self, name):
       for i in range (10):
            time.sleep(0.5)
            print(f'This is {name}')

Compressor1 = VideoCompressor()
q = queue.Queue(5)
def add_thread(name):

    current_thread_number = threading.active_count()
    print(current_thread_number)
    t = Compressor1.execute(str(name))
    if current_thread_number < 6:
        t.start()
    if current_thread_number >= 6:
        q.put(t)
        print('added')
    return t
thread_list = []

for i in range(9):
    thread_list.append(add_thread(f'test_{i}.mp4'))

while not q.empty():
    current_thread_number = threading.active_count()
    if current_thread_number < 6:
        t = q.get()
        t.start()

for thread in thread_list:
    if thread.is_alive():
        thread.join()

print(q.queue)
print('end')



# os.system(f'ffmpeg -i {name} -b:v 2M -b:a 192k -filter:v fps=fps=30 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {name}_output.avi')


