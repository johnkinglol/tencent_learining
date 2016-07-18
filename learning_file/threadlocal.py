#!/usr/bin/env python
# coding=utf-8
import threading


# create obj
thread_local = threading.local()

def process_student():
    std = thread_local.student

    print("hello, %s from %s" % (std, threading.currentThread().name))

def process_thread(name):
    thread_local.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=("zhaodeng", ), name="Thread-1")
    t2 = threading.Thread(target=process_thread, args=("john", ), name="Thread-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
