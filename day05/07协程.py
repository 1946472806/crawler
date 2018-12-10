
#协程一个简单实现
import time

#生成器函数
def C():
    while True:
        print('=========C===============')
        yield
        time.sleep(0.5)
#普通函数
def D(c):
    while True:
        print('=========D===============')
        next(c)
        time.sleep(0.5)
if __name__=="__main__":
    c = C() #c是generator对象
    D(c)