import multiprocessing

def fn(*args):
    #进程名称
    name = multiprocessing.current_process().name
    #进程id
    pid = multiprocessing.current_process().pid
    print('子进程:' ,name,pid)


if __name__ == '__main__':
    #创建进程
    p1 = multiprocessing.Process(target=fn,args=('李小璐','PGone'),name='进程1')
    p2 = multiprocessing.Process(target=fn, args=('李小璐', '薛之谦'),name='进程2')
    #守护进程
    # p1.daemon = True
    p1.start()
    # p1.join() #同步
    p2.start()