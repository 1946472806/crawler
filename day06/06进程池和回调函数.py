import multiprocessing
import random
import time


def fn1():
    print('进程1开始')
    time.sleep(random.randint(2,5))
    print('进程1结束')
    return 'fn1'
def fn2():
    print('进程2开始')
    time.sleep(random.randint(2,5))
    print('进程2结束')
    return 'fn2'
def fn3():
    print('进程3开始')
    time.sleep(random.randint(2,5))
    print('进程3结束')
    return 'fn3'
def fn4():
    print('进程4开始')
    time.sleep(random.randint(2,5))
    print('进程4结束')
    return 'fn4'
def fn5():
    print('进程5开始')
    time.sleep(random.randint(2,5))
    print('进程5结束')
    return 'fn5'

#回调函数
def cb(result):
    print('回调函数被调用',result)

if __name__ == '__main__':
    #创建进程池,进程池中的进程数量最多为2个
    pool = multiprocessing.Pool(2)
    fn_list = [fn1,fn2,fn3,fn4,fn5]
    for i in fn_list:
        # #同步
        # pool.apply()
        #异步
        pool.apply_async(i,callback=cb)

    #必须先关闭进程池才能调用进程池中的进程
    pool.close()

    pool.join()