#!/usr/bin/env python
# coding=utf-8
import threading, time

#run code for new thread
def loop():
    print("thread %s is running(in loop)..." % threading.currentThread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.currentThread().name, n))
        time.sleep(1)
    print("thread %s ended" % threading.currentThread().name)

if __name__ == '__main__':
    print("thread %s is running(out loop)..." % threading.currentThread().name)
    t = threading.Thread(target=loop, name='zhaodeng-Thread')
    t.start()
    t.join()
    print("thread %s is ended." % threading.currentThread().name)