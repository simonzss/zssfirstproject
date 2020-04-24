# 生产者与消费者：两个线程之间的通信
# 注意这不是数据共享问题，这是一个线程生产出的数据供另一个线程使用的问题
# Python的Queue模块提供了同步的、线程安全的队列类，包括先进先出的队列Queue，后进先出的队列LifoQueue
# 以及优先级队列PriorityQueue，这些队列都实现了锁的原理，可以用来安全实现线程间的同步

import threading,queue,random,time

def produce(q):
    i=0
    while i<10:
        num=random.randint(0,100)
        q.put(num)
        print('生产者生产数据{}'.format(num))
        time.sleep(1)
        i+=1
    q.put(None)
    q.task_done()

def consume(q):
    while True:
        item=q.get()
        if item==None:
            break
        print('消费者获取到数据{}'.format(item))
        time.sleep(4)
    q.task_done()



if __name__ == '__main__':
    q=queue.Queue(5)  # 通过限制Queue队列的长度，可以观察到生产者等待消费者拿走后才能产生下一个数据的现象，线程是安全的
    # 创建生产者
    p=threading.Thread(target=produce,args=(q,))
    p.start()
    # 创建消费者
    c=threading.Thread(target=consume,args=(q,))
    c.start()

    p.join()
    c.join()
    print('END')

'''
start()方法的理解
p=threading.Thread(target=produce,args=(q,)) 
p.start()
start()方法会开新线程，然后去执行run()里面的动作，所有的动作都要放到run()里面，包括target=produce中的produce
程序底层会将produce自动传给run()
'''
