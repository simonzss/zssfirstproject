# 线程中的GIL 全局解释器锁 在多个线程使用共享数据的情境下需要考虑锁的问题
# 线程使用场景：耗时操作，如爬虫、IO         进程使用场景：计算密集型
# python底层默认线程的共享数据统一加锁，保证数据安全性。但数据量大的时候会自动取消锁
import threading

lock=threading.Lock()

n=0
def task1():
    global n
    for i in range(1000000):
        n+=1
    print('task1中的n值是{}'.format(n))

def task2():
    global n
    for i in range(1000000):
        n+=1
    print('task2中的n值是{}'.format(n))

if __name__ == '__main__':
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('n的最终值是{}'.format(n))  # 最终结果值不是200万

# 线程同步的概念   多个线程共享数据时，为了保证共享数据的准确性，就需要对多个线程进行同步，要用到线程锁
# 所谓同步，就是一个一个完成，一个完成了另一个才能进来
# 线程锁：使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire和release方法
# 对于需要每次只允许一个线程造作的数据，可以将其操作放到acquire和release方法之间
# 注意 线程锁与全局解释器锁是不同的，线程锁是程序员设置的，全局解释器锁是python解释器自带的

m=0
def task3():
    global m
    lock.acquire()
    for i in range(1000000):
        m+=1
    print('task3中的m值是{}'.format(m))
    lock.release()

def task4():
    global m
    lock.acquire()
    for i in range(1000000):
        m+=1
    print('task4中的m值是{}'.format(m))
    lock.release()

if __name__ == '__main__':
    t3=threading.Thread(target=task3)
    t4=threading.Thread(target=task4)
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print('m的最终值是{}'.format(m))  # 给task3和task4加锁后，m值为200万