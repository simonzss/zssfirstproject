# 使用gevent实现协程
import time

import gevent
from gevent import monkey

#monkey.patch_all()

def a():
    for i in range(5):
        print('A'+str(i))
        time.sleep(0.5)

def b():
    for i in range(5):
        print('B'+str(i))
        time.sleep(0.5)

def c():
    for i in range(5):
        print('C'+str(i))
        time.sleep(0.5)

g1=gevent.spawn(a) # Create a new :class:`Greenlet` object and schedule it to run ``function(*args, **kwargs)``
g2=gevent.spawn(b)
g3=gevent.spawn(c)
g1.join()
g2.join()
g3.join()  # 类似于gevent.joinall(a,b,c)

# 以上代码并没有实现协程并行，因为gevent并不知道哪里是IO语句
# 生成器中，我们用yield告诉程序哪里要切换，greenlet中，我们用switch()告诉程序哪里要切换
# 这里我们用monkey模块的patch_all()方法让程序自动识别哪里要切换，monkey会自动将类似sleep这类的语句识别为IO操作