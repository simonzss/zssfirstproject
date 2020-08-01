# 进程池  进程池是依赖于主进程的，主进程执行完毕结束后，进程池就会结束，因此需要用join()来暂时挡住主进程为pool争取执行时间
# 非阻塞式  将进程全部添加到进程池中，一个进程任务完毕后立刻执行下一个任务，无需等待其他的进程完毕,也无需等待callback
# 阻塞式  任务依次执行，上一个任务不完成，下一个任务就不会开始，进程由001-002-003-004-005-001-002循环使用
# 注意，回调函数callback是单独的进程
# apply_async 非阻塞式  apply阻塞式  非阻塞式用得较多，阻塞式其实就是串联电路模式
# 回调函数的英文定义如下，本人现有水平暂不赞成回调函数一定是后于主函数执行的说法
# In computer programming, a callback, also known as a "call-after" function,
# is any executable code that is passed as an argument to other code;
# that other code is expected to "call back" (execute) the argument at a given time.
import os
import time
from multiprocessing.pool import Pool
from random import random


def task(task_name):
    print('开始做*{}*任务啦~'.format(task_name))
    start=time.time()
    time.sleep(random()*2)
    end=time.time()
    return '完成*{}*任务用时{},进程id为{}'.format(task_name,end-start,os.getpid())

# 定义回调函数,回调函数会接收任务函数task的return值，并可在回调函数内部作处理
contain=[]
def callback_func(n):
    contain.append(n)
    contain.append(os.getpid())


if __name__ == '__main__':
    pool=Pool(5)
    task_list=['吃饭','睡觉','打豆豆','打游戏','带孩子','喝水','跑步','旅行']
    for i in task_list:
        pool.apply_async(task,(i,),callback=callback_func)
        # pool.apply_async(任务函数名,任务函数参数(,),回调函数名callback=)

    pool.close() # 表示添加任务结束，关闭pool
    pool.join()  # 让主进程让步，以便进程池完成任务
    for i in contain:
        print(i)
    print('over~~~~')

# 进程间的通信  Queue队列的使用  .put()  .get()  .put_nowait()  .get_nowait()

from multiprocessing import Queue

q=Queue(5)

q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.get())

if not q.full(): # q.full()用来判断Queue队列是否已满，对应的有q.empty()
    q.put('F')
else:
    print('Queue队列已满')
print(q.qsize())  # 注意这句，程序多处出现qsize的值恰恰说明队列能够被多个线程所访问到
# q.put('F') q的上限为5个，如果有第六个'F',Queue队列就会一直等待，直到前5个有一个被取走后才能put进第六个'F'
# q.put('F',timeout=3) # 注意timeout的使用，3秒后会抛出异常queue.Full，因此常与try&except结合使用

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())