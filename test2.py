from multi_thread_worker import MultiThreadWorker
mtw4 = MultiThreadWorker(2, 10)
mtw4.add_task('@Shakespeare', 5)
mtw4.start()