import threading
import time

#信号量：允许的线程最大并发量3
sem = threading.Semaphore(3)

def fn():
    with sem:
        print('子线程%s开始执行...' % threading.current_thread().name)
        time.sleep(3)
        print('子线程%s结束...' % threading.current_thread().name)

if __name__=="__main__":
    for i in range(20):
        t = threading.Thread(target=fn)
        t.start()