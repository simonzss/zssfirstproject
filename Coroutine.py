# 协程：是单线程下的并发，又称微线程，一旦遇到io，就会从应用程序级别（而非操作系统）控制切换
# 操作系统控制'线程'的切换，用户在单线程内控制'协程'的切换
import time

from greenlet import greenlet


def task1():
    for i in range(3):
        print('A' + str(i))
        yield  # return加暂停
        time.sleep(0.5)


def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()
    while True:
        try:
            g1.__next__()
            g2.__next__()
        except:
            break

print()
print('************************')

# 用greenlet实现协程
def a():
    for i in range(5):
        print('A'+str(i))
        gb.switch()
        time.sleep(0.5)

def b():
    for i in range(5):
        print('B'+str(i))
        gc.switch()
        time.sleep(0.5)

def c():
    for i in range(5):
        print('C'+str(i))
        ga.switch()
        time.sleep(0.5)

if __name__ == '__main__':
    ga=greenlet(a)
    gb=greenlet(b)
    gc=greenlet(c)

    ga.switch()  #  If this greenlet has never been run, then this greenlet
                 #  will be switched to using the body of self.run(*args, **kwargs).