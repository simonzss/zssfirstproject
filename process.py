# 进程  线程  协程
# 并发和并行
# 程序是指令、数据及其组织形式的描述，进程是程序的实体。
# 进程间是相互独立的，进程是由操作系统分配的，开销比较大，可创建的进程数量是有限的
# 用multiprocessing中的Process来创建进程

import os
from multiprocessing import Process
from time import sleep


def task1(name):
    while True:
        sleep(1)
        print('task1----------------------', os.getpid(), '---->', os.getppid(),name)


def task2(name):
    while True:
        sleep(2)  # os.getpid()得到当前进程id                        # os.getppid()得到父进程id
        print('task2----------------------', os.getpid(), '---->', os.getppid(),name)


if __name__ == '__main__':  # 当运行本程序时，本程序自动被创建为一个进程，这个进程是父进程
    print(os.getpid())  # 得到当前进程id
    p1 = Process(target=task1, name='任务1',args=('aa',))  # 在父进程中创建子进程1
    p1.start()
    p2 = Process(target=task2, name='任务2',args=('bb',))  # 在父进程中创建子进程2 # args=('bb',)以元组形式传参
    p2.start()
    # p2.run() # run是只执行任务而不启动进程，start是启动进程来执行任务
    # p2.terminate() 用来结束进程

'''
注意，并'不存在'父进程执行完毕再执行子进程的顺序，本例是因为子进程有sleep动作
父子进程谁先被执行取决于cpu的执行，涉及底层原理，不必追究
多进程对于全局变量的访问，在每一个进程中都会独立一份全局变量，保证每个进程访问变量互不干扰
无论这个全局变量是可变的还是不可变的，每个进程都会独立一份，保证每个进程访问变量互不干扰
'''

# 进入自定义进程部分

class MyProcess(Process):

    def __init__(self,name):
        super(MyProcess, self).__init__()
        self.name=name

    # 重写run方法
    def run(self) -> None:
        n=1
        while True:
            print('自定义进程名:{}------n值为{}'.format(self.name,n))
            n+=1
            if n==10000:
                break

if __name__ == '__main__':
    p=MyProcess('小明')
    p.start()  # start的作用,1是开新的进程，2是执行进程里的run()方法

    p1=MyProcess('小华哗哗哗')
    p1.start()
