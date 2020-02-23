from multi_thread_worker import MultiThreadWorker


def test_normal():
    num_workers = 6
    queue_size = 100
    num_tweets = 10

    userlist1 = [
        '@Shakespeare',
        '@realDonaldTrump',
        '@Literature',
        '@langston_poems']
    mtw1 = MultiThreadWorker(num_workers, queue_size)
    for user in userlist1:
        mtw1.add_task(user, num_tweets)
    assert mtw1.start() == 0

    userlist2 = ['@langston_poems']
    mtw2 = MultiThreadWorker(num_workers, queue_size)
    for user in userlist2:
        mtw2.add_task(user, num_tweets)
    assert mtw2.start() == 0

    userlist3 = ['@Shakespeare', '@realDonaldTrump']
    mtw3 = MultiThreadWorker(num_workers, queue_size)
    for user in userlist3:
        mtw3.add_task(user, num_tweets)
    assert mtw3.start() == 0


def test_overload():
    num_workers = 2
    queue_size = 100
    num_tweets = 10
    userlist4 = [
        '@Shakespeare',
        '@realDonaldTrump',
        '@Literature',
        '@langston_poems']
    mtw4 = MultiThreadWorker(num_workers, queue_size)
    for user in userlist4:
        mtw4.add_task(user, num_tweets)
    assert mtw4.start() == 0


def main():
    pass


if __name__ == "__main__":
    main()
