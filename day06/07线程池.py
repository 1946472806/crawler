import random
import threading
import time

import threadpool


def fn(arg):
    name = threading.current_thread().name
    print('子线程开始:',name,arg)
    time.sleep(random.randint(2,5))
    print('子线程结束:',name,arg)
    return '子线程结束:'+ name + arg

#回调函数
def cb(request,result):
    print('回调函数被调用',result)

if __name__ == '__main__':
    #创建线程池,线程池中线程最多为3个
    pool = threadpool.ThreadPool(3)

    arg_list = ['李小璐','马蓉','宝强','薛之谦','荣哲','陈羽凡']
    requests = threadpool.makeRequests(fn,arg_list,callback=cb)

    #把8个请求，加入线程池
    for request in requests:
        pool.putRequest(request)
    pool.wait()