import threading
import time
import sys
import os

def thread_hello(name):
    print('hello {} !'.format(name))
    time.sleep(10)
    print('thread t1 exits...')
    return

def thread_operation():
    t = threading.currentThread()
    print("thread name : {}".format(t.name))
    time.sleep(20)
    print("{} exits... ".format(t.name))

t1 = threading.Thread(targot=thread_hello,args=('Kim',))
t1.start()

t2 = threading.Thread(target=thread_operation,name='Second thread',args=())

t2.setDaemon(True)
t2.start()

print("main thread exits...")