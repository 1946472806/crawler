import multiprocessing


#自定义进程
import os


class MyProcess(multiprocessing.Process):
    def __init__(self,name,url):
        super().__init__()
        self.name = name
        self.url = url

    #重写run
    def run(self):
        print('子进程:',self.name)
        print('子进程id:',os.getpid())
        print('父进程id:', os.getppid())

if __name__ == '__main__':
    p1 = MyProcess('特朗普','http://www.baidu.com')
    p2 = MyProcess('詹姆斯', 'http://www.qq.com')
    p1.start()
    p2.start()

    print('主进程id:',multiprocessing.current_process().pid)

    print(multiprocessing.cpu_count()) #CPU数量

    #正在运行的子进程
    print(multiprocessing.active_children())