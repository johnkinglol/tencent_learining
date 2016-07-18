#!/usr/bin/env python
# coding=utf-8
import random, time, queue
from multiprocessing.managers import BaseManager


# the queue for sending task
task_queue = queue.Queue()
# the queue for receiving the task
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue
if __name__ == '__main__':
    # register two queues, use called to set the param
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # binding 5000 port, set verify code 'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # start Queue
    manager.start()

    # get Queue object through internet
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # put task
    for i in range(10):
        n = random.randint(0, 10000)
        print("Put task %d..." % n)
        task.put(n)

    time.sleep(10)
    print("Try get results...")
    for i in range(10):
        r = result.get(timeout=10)
        print("Result: %s" % r)

    #close
    manager.shutdown()
    print("master exit.")