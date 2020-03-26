
# 闭包
import time


def func(number):
    a=100
    def inner_func():
        nonlocal a
        for i in range(number):
            a+=1
        print(a)
        print('以上是演示闭包的应用')
    return inner_func

x=func(5)
x()

# 装饰器
# 特点：1、函数A是作为参数出现的（函数B就接收函数A作为参数）
# 特点：2、要有闭包的特点
print('-----------装饰器的应用-----------')
def decorate(func):
    def wrapper():
        print('1.装饰器通过函数参数，接收到了被装饰函数house，开始对house进行处理，先打印本消息说明开始处理')
        print('2.',func)
        print('3.对函数参数house进行了刷漆...')
        print('4.对函数参数house进行了铺地板...')
    return wrapper

@decorate  #1.将被装饰函数house作为参数传给装饰器  2.在底层'执行'装饰器函数  3.将装饰器函数返回值又赋回给被装饰函数house
def house():
    print('我有一个毛坯房......')


house    # 这里的house等于wrapper，不执行就没有结果
house()  # 这里的wrapper()，执行了就有结果

# 万能装饰器
print('.............以下是万能装饰器部分.................')

# 定义万能装饰器
def decorate_all(func):
    def wrapper(*args,**kwargs):   # 这里是定义函数，*和**代表的是装包
        print('已开始对下一行所示的被装饰函数进行装饰...')
        print(func)    # <function f1 at 0x00000277DD9530D0>
        time.sleep(3)
        print('对被装饰函数装饰完毕')
        func(*args,**kwargs)
        print(wrapper)    # <function decorate_all.<locals>.wrapper at 0x00000277DD953040>
        print('.......................')
    return wrapper

@decorate_all
def f1():
    print('执行了无参函数f1')
    print(f1)           # <function decorate_all.<locals>.wrapper at 0x00000277DD953040>

@decorate_all
def f2(int1):
    print('执行了单参数函数f2,打印一个整型数',int1)

@decorate_all
def f3(name,age):
    print('执行了双参数函数f3,打印出姓名和年龄',name,age)

list1=['lily','tom','jerry','fly']
@decorate_all
def f4(list1,age=20):
    for i in list1:
        print('执行了带列表参数加关键字参数的函数f4,打印出list1里的姓名和年龄',i,age)

f1()
f2(3)
f3('tom',20)
f4(list1,30)



