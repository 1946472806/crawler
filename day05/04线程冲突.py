

#操作一个数据
import threading

m = 0

def add():
    global m
    for i in range(1000000):
        m += 1
        m -= 1
    print(m)

#线程冲突
def conflict():
    for i in range(5):
        t = threading.Thread(target=add)
        t.start()

#解决多个线程同时处理一个数据造成冲突的情况
#方式一：线程同步
def thread_sync():
    for i in range(5):
        t = threading.Thread(target=add)
        t.start()
        t.join()
#方式二：线程锁
#lock():普通锁
#RLock():递归锁
lock = threading.Lock()
def add2():
    global m

    #方式一：手动加、解锁
    # #加锁
    # if lock.acquire(): #如果上锁了，则执行下面的代码
    #     for i in range(1000000):
    #         m += 1
    #         m -= 1
    # #解开锁
    # lock.release()
    
    #方式二：自动加、解锁
    with lock:
        for i in range(1000000):
                m += 1
                m -= 1

    print(m)
def thread_lock():
    for i in range(5):
        t = threading.Thread(target=add2)
        t.start()

if __name__=="__main__":
    # conflict()
    # thread_sync()
    thread_lock()