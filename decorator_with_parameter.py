# 带参数的装饰器

def outer(num):   # 第一层，负责接收装饰器的参数
    def decorate(func):  # 第二层，负责接收被装饰的函数
        def wrapper(*args,**kwargs):  # 第三层，负责接收被装饰的函数带来的参数
            func(*args,**kwargs)
            print('铺了{}块地砖......'.format(num))
        return wrapper
    return decorate


@outer(5)
def house():
    print('我是一个毛坯房......')

house()