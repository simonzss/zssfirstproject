import sys


# 魔术方法 __new__ 魔术方法，能够在特定的时候自动触发，不需要调用

class Person:

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('------__new__')


p = Person('jack')
# print(p.name) 此句报错因此注释掉以执行Person1


# 注意以上这一段代码，我们用自定义的__new__方法覆盖了系统给我们提供的__new__方法，系统的__new__方法是用来创建并返回对象的
# 因此我们自定义的__new__方法只打印字符串，没有返回任何对象，因此p=Person()这里本来要求有参数的也不会报错了
# 再来用带参数的形式，p=Person('jack')，虽然形式正确，但我们自定义的__new__方法还是不会返回对象
# 因此再执行print(p.name)，会得到错误：AttributeError: 'NoneType' object has no attribute 'name'
# 因为我们此时由类创建对象p都做不到了，没有对象自然就没有对象p的属性
# 我们进行改良如下

print()
print('开始Person1的例子')
print()


class Person1:

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('------__new__用来生产对象')
        print('这就是类所产生的对象的地址:', object.__new__(cls))  # 这就是类所产生的对象的地址
        return object.__new__(cls)  # 这里我们找回了系统的原生__new__方法

    def __call__(self, *args, **kwargs):
        print('你执行了p1()，将对象作为函数直接调用啦~')


p1 = Person1('jack')
print(p1.name)

# 这里我们找回了系统的原生__new__方法，因此恢复了系统的正常功能,p1这个对象正常生成，并打印了对象属性name

# ******************__new__方法的总结***********************
'''
类的__new__方法是用来创建对象的，实际开发中，很少对__new__方法进行改动
执行Person()时，最先执行的一定是__new__方法，__new__方法以返回值的方式新开辟一块内存空间地址，这个地址就是对象地址
__new__方法以类自身(cls)为参数，以对象为返回值，这个对象返回值直接传给__init__方法
__init__方法的self参数接住这个对象返回值，开始赋值给对象的属性，本例中对象的属性是self.name = name
执行完__init__方法后，对象创建完成
如果有p1=Person()，那么将创建完成的对象赋给p1这个变量

'''
print()
print('以下是__call__方法')
# 如果执行p1()，会得到TypeError: 'Person1' object is not callable
'''
对象的使用方法一般是p1.属性   p1.方法   用.来调用
如果想把对象当成函数使用，直接用p1()来实现一些功能，就要重写__call__方法
'''
p1()


###############       __del__方法         #################
print()
print('以下是__del__方法:')


class Person2:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('执行__del__方法，注意不是del方法')


# getrefcount()的作用是，返回有多少个'变量名'引用了同一个对象内存地址
p2 = Person2('jack')
print(sys.getrefcount(Person2('jack')))  # 结果为1,注意Person2('jack')并不是一个'变量名'
print(sys.getrefcount(p2))  # 结果为2  # 注意getrefcount()函数自身也引用对象p2的地址，故引用数量为2个

n = p2
n1 = p2
print(sys.getrefcount(Person2('jack')))  # 结果仍为1,注意Person2('jack')并不是一个'变量名'
print(sys.getrefcount(p2))  # 结果为4  # 注意getrefcount()函数自身也引用对象p2的地址，故引用数量为4个

x = n1
print(sys.getrefcount(x))  # 结果为5，x这个变量名引用的内存地址，共有5个变量名引用这个内存地址:p2,n,n1,x以及sys.getrefcount

'''
1、对象赋值的概念
   p=Person()
   p1=p
   说明p和p1共同引用同一个地址
2、删除地址的引用
   del p1  删除p1对地址的引用
3、查看对地址的引用次数：
   import sys
   sys.getrefcount(p)
4、当一块空间没有了任何引用，ref=0时，默认执行__del__，这涉及程序底层的垃圾回收机制
   当一个python文件执行完毕后，系统会启动垃圾回收
   注意到本例中，__del__被启动了多次，垃圾回收机制因水平有限还不清楚，因此不建议自己重写__del__
'''
