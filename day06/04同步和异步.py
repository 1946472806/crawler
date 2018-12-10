import multiprocessing
import random
import time


def fn1():
    time.sleep(random.randint(1,3))
    print('子进程:',multiprocessing.current_process().name)

def fn2(lock):
    pname = multiprocessing.current_process().name
    print('进程开始:',pname)
    with lock:
        print('开始...')
        time.sleep(random.randint(1, 3))
        print('结束...')
    print('进程结束:', pname)

if __name__ == '__main__':
    #异步
    # p1 = multiprocessing.Process(target=fn1).start()
    # p2 = multiprocessing.Process(target=fn1).start()

    # 同步
    # p1 = multiprocessing.Process(target=fn1)
    # p2 = multiprocessing.Process(target=fn1)
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()

    #进程锁
    lock = multiprocessing.Lock()

    p3 = multiprocessing.Process(target=fn2,args=(lock,),name='金三胖')
    p4 = multiprocessing.Process(target=fn2,args=(lock,),name='罗4炮')
    p3.start()
    p4.start()