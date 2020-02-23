import queue
import threading
from tweet2video import Tweet2Video


class MultiThreadWorker():
    def __init__(self, num_workers, queue_size):
        self.num_workers = num_workers
        self.queue_size = queue_size
        self.q = queue.Queue(queue_size)
        self.active_works = []

    def add_task(self, username, num_tweets):
        t = threading.Thread(
            target=self.generate_video,
            args=(username, num_tweets))

        num_active_workers = threading.active_count() - 1
        # print(num_active_workers)
        if num_active_workers < self.num_workers:
            t.start()
            self.active_works.append(t)
        else:
            self.q.put(t)
            print(f'{username} is waiting.')
        return t

    def generate_video(self, username, num_tweets):
        tv = Tweet2Video(username, num_tweets)
        print(f'{username} starts.')
        tv.run()
        print(f'{username} done.')

    def start(self):
        while not self.q.empty():
            num_active_workers = threading.active_count()
            # print('num_active_workers', num_active_workers)
            if num_active_workers < self.num_workers:
                t = self.q.get()
                t.start()

        for worker in self.active_works:
            if worker.is_alive():
                worker.join()
        return 0


def main():
    num_workers = 2
    queue_size = 100
    mtw = MultiThreadWorker(num_workers, queue_size)
    mtw.add_task('@Shakespeare', 10)
    mtw.add_task('@realDonaldTrump', 10)
    mtw.add_task('@Literature', 10)
    mtw.add_task('@langston_poems', 10)
    mtw.start()


if __name__ == '__main__':
    main()
