#!/usr/bin/env python
# coding=utf-8
import time, sys, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

# get Queue as name
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

# begin to connect server
server_addr = '127.0.0.1'
print("Connect to server %s..." % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

# get Queue
task = m.get_task_queue()
result = m.get_result_queue()

# get task from task queue, and put into result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("Run task %d * %d" % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("task queue is empty")

print("worker exit.")
