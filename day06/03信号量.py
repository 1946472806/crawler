import multiprocessing
import time

#控制进程最大的并发量为3
sem = multiprocessing.Semaphore(3)

def fn():
    with sem:
        panem = multiprocessing.current_process().name
        print('子进程开始:',panem)
        time.sleep(2)
        print('子进程结束:', panem)

if __name__ == '__main__':
    for i in range(1,11):
        multiprocessing.Process(target=fn).start()