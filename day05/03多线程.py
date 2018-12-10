import random
import threading
import time


def fn(*args):
    time.sleep(random.randint(1,3))
    print('子线程:',args)

def create_thread():
    # t1 = threading.Thread(target=fn,args=('百合',))
    # t1.start()
    # t2 = threading.Thread(target=fn, args=('强东',))
    # t2.start()
    # t3 = threading.Thread(target=fn, args=('抹茶',))
    # t3.start()

    t_list = []
    for i in range(1,4):
        t = threading.Thread(target=fn, args=('百合'+str(i),))
        t.start()

        #同步执行,会阻塞主线程
        # t.join() #等待上面的线程执行完毕，然后再继续执行下一个线程

        print(t.ident) #线程id
        print(t.isAlive())#线程是否正在活动运行
        print(t.isDaemon())#线程是否为守护线程
        print(threading.active_count())#正在运行的线程数量
        print(threading.enumerate())#正在运行的线程列表

        t_list.append(t)

    #保证所有线程执行完毕
    for t in t_list:
        t.join()

    print('主线程执行完毕...')
if __name__=="__main__":
    create_thread()