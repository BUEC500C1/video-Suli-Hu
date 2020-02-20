import queue
import threading
import numpy as np
import time
import os

import compress as comp

class VideoCompressor():

    def __init__ (self, pool_size = 3, queue_size = 10):
        self.pool_size = pool_size
        self.queue_size = queue_size

    def execute(self, username, picpath, numOfTweets):
        t = threading.Thread(target = self.compress, args = (username, picpath, numOfTweets) )
        return t

    def compress(self, username, picpath, numOfTweets):
        comp.tweet2video(username, picpath, numOfTweets)
        for i in range (10):
            time.sleep(0.5)
            print(f'This is {username}')


def add_thread(username, picpath, numOfTweets):
    current_thread_number = threading.active_count()
    print(current_thread_number)
    t = Compressor1.execute(username, picpath, numOfTweets)
    if current_thread_number < 6:
        t.start()
    if current_thread_number >= 6:
        q.put(t)
        print('added')
    return t

def compressVideo(userlist,numOfTweets):
    
    q = queue.Queue(100)
    thread_list = []
    
    for user in userlist:
        thread_list.append(add_thread(user, './pic_'+user+'/', numOfTweets))

    while not q.empty():
        current_thread_number = threading.active_count()
        if current_thread_number < 6:
            t = q.get()
            t.start()

    for thread in thread_list:
        if thread.is_alive():
            thread.join()

    print(q.queue)
    print(f'thread_list:{thread_list}')
    print('end')
Compressor1 = VideoCompressor()
u1 = ['@Shakespeare','@realDonaldTrump', '@Literature', '@langston_poems']
compressVideo(u1,10)
# os.system(f'ffmpeg -i {name} -b:v 2M -b:a 192k -filter:v fps=fps=30 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {name}_output.avi')




# comp.tweet2video('@Shakespeare','./pic/',6)














# name = '@Shakespeare'
# #name = '@realDonaldTrump'
# tweet1 = twt.get_all_tweets(name,10)
# for i in range(len(tweet1)):
#     twt.textToImg(twt.deEmojify(tweet1[i]),name,i)
# if os.path.exists('./pic/.DS_Store'): 
#     os.remove('./pic/.DS_Store')
# cytwt.makevideo('./pic/',name)



