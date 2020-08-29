# 作用域  LEGB规则
# L Local
# E Enclosing  封闭
# G Global
# B Built-in  内置的
import sys

a=100

def func():
    a=10

    def inner_func():
        a=1
        print(a)
        print(max)   # 内置的  并未在本文件中定义
        # print(dir())
        print("inner_func内的locals：",dir())
        # print(globals())

    print("func内的locals：",dir())
    inner_func()

func()
print("本模块内的locals：",dir())

def f1():
    nnn=666
    print('666')

def diaoyong(aaaaa=10):
    b=9
    f1()
    print("diaoyong模块内的locals：", locals())

diaoyong()
print("本模块内的locals：",dir())
print(globals())

def make_incrementor(n):
    print("make_incrementor内的locals：", dir()) # lambda可以引用n
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

def myadd(a=0,b=1,*args):
    print(a,b,args)

myadd()
myadd(3,4,5,6)

def foo(name1, **kwds):
    print(kwds)
    print(name1)
    print(locals())
    return 'name' in kwds

print(foo(1,a=1,b=2,name=3))

def fff(ham: str, eggs: str = 'eggs2') -> str:
     print("Annotations:", fff.__annotations__)
     print("Arguments:", ham, eggs)
     return ham + ' and ' + eggs

fff('spam1')

print(sys.path)