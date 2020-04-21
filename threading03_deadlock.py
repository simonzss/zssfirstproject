# 死锁
# 开发过程中在多个线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源时，就会造成死锁
# 避免死锁的方法  1、重构  2、给require()加上timeout参数

from threading import Thread,Lock
from time import sleep

lockA=Lock()
lockB=Lock()

class Thread1(Thread):  # 自定义线程，与自定义进程格式上类似
    def run(self) -> None:
        if lockA.acquire():
            print('{}获取了A锁'.format(self.name))
            sleep(0.1)
            if lockB.acquire():
                print('{}获取了B锁,并同时拥有A锁'.format(self.name))
                lockB.release()
            lockA.release()

class Thread2(Thread):
    def run(self) -> None:
        if lockB.acquire():
            print('{}获取了B锁'.format(self.name))
            sleep(0.1)
            if lockA.acquire():
            # if lockA.acquire(timeout=1): # 这一句通过timeout使得Thread-2在1秒后不再等待A锁，程序得以继续执行后续语句释放B锁
                print('{}获取了A锁,并同时拥有B锁'.format(self.name))
                lockA.release()
            lockB.release()

if __name__ == '__main__':
    t1=Thread1()
    t2=Thread2()
    t1.start()
    t2.start()
    t1.join()
    t2.join()

'''
以上代码就是一个典型的死锁，通过sleep语句实现了两个线程分别拥有A锁和B锁，并同时等待对方锁释放
修改方式有两种，要么重构代码，要么加上timeout
'''