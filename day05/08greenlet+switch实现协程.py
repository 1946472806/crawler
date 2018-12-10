import time
from greenlet import greenlet

# greenlet.switch()
def fn1():
    print('协程1')
    time.sleep(2)
    g2.switch()


    print('床前明月光')
    time.sleep(2)
    g2.switch()

    print('举头望明月')

def fn2():
    print('协程2')
    time.sleep(2)
    g1.switch()


    print('疑是地上霜')
    time.sleep(2)
    g1.switch()


if __name__=="__main__":
    g1 = greenlet(fn1)
    g2 = greenlet(fn2)
    g1.switch() #切换到g1