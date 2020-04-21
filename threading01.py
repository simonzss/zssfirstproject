# 线程 threading
# 一个进程可以有多个线程，常用来执行延时任务
# 线程有三个状态，就绪、运行、阻塞，其中，执行了start()之后就进入就绪状态，等待cpu调用
# 运行 cpu执行了线程后线程进入运行状态，注意，多个线程没有进入cpu的先后顺序，谁先被cpu执行是不清楚的
# 阻塞，当线程暂停执行时进入阻塞状态，如遇到sleep语句时。注意，阻塞解除后是回到就绪状态等待调用，不是回到运行状态
from time import sleep

import threading

def download(n):
    images=['boy.jpg','girl.jpg','animal.jpg']
    for i in images:
        print('正在下载{}...'.format(i))
        sleep(n)
        print('{}下载完成'.format(i))

def listenmusic(n):
    musics = ['成都', '总有一天等到你', '上海滩']
    for i in musics:
        print('正在听歌{}...'.format(i))
        sleep(n)
        print('{}听歌完成'.format(i))

if __name__ == '__main__':
    t1=threading.Thread(target=download, args=(1,))
    t2=threading.Thread(target=listenmusic, args=(0.5,))
    t1.start()
    t2.start()
    t1.join()  # 注意，加入join后可以确保先于抢票线程完成
    t2.join()
# 线程可以共享全局变量，这点与进程不同
# 抢票
ticket=1000

def buy_ticket():
    global ticket
    for i in range(100):
        ticket-=1
        print('现有票数:{}'.format(ticket))

t1=threading.Thread(target=buy_ticket)
t2=threading.Thread(target=buy_ticket)
t3=threading.Thread(target=buy_ticket)
t4=threading.Thread(target=buy_ticket)
t1.start()
t2.start()
t3.start()
t4.start()

