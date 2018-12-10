import _thread
import threading
import time


def fn(args):
    time.sleep(2)
    print('我是在子线程中执行...')
    print('args:',args)
    print('子线程名称:',threading.current_thread().name)

#方式一
def create_thread1():
    #这种方式创建的线程是守护线程,如果主线程结束,则守护线程也立刻结束.
    _thread.start_new_thread(fn,('李小璐',))

    #让主线程不结束
    while True:
        time.sleep(2)

#方式二(推荐)
def create_thread2():
    #创建线程(默认不是守护线程)
    #daemon=True:是否设置为守护线程
    # t = threading.Thread(target=fn,name='thread2',args=('陈羽凡',),daemon=True)
    t = threading.Thread(target=fn, name='thread2', args=('陈羽凡',))
    t.start() #启动线程
    # t.join() 加上这句话表示主线程会等子线程执行完再执行下面的结束执行语句
    print(threading.current_thread().name) #主线程名称 MainThread
    print('主线程结束...')

#方式三（自定义线程，继承自threading.Thread）
class myThread(threading.Thread):
    def __init__(self,name,task,subtask):
        super().__init__()

        self.name = name
        self.task = task
        self.subtask = subtask

    #重写run
    def run(self):
        print('子线程:',self.name,self.task,self.subtask)
def create_thread3():
    mt = myThread("小分队I", "巡山", "扫黄")
    mt.start()
    print(threading.current_thread().name)
    print('主线程结束...')
if __name__=="__main__":
    create_thread3()