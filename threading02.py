# 线程中的GIL 全局解释器锁 在多个线程使用共享数据的情境下需要考虑锁的问题
# 线程使用场景：耗时操作，如爬虫、IO         进程使用场景：计算密集型
# python底层默认线程的共享数据统一加锁，保证数据安全性。但数据量大的时候会自动取消锁
import threading

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
    t3=threading.Thread(target=task1)
    t4=threading.Thread(target=task2)
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print('n的最终值是{}'.format(n))  # 最终结果值不是200万