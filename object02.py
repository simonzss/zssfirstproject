# 类的方法：普通方法  类方法  静态方法  魔术方法

# 普通方法
class Phone:
    brand = 'xiaomi'
    price = 4999
    mode = 'TD-LTE'

    def call(self):
        print('self的地址是', self)
        print('开始打电话')


p1 = Phone()
print('当前对象的地址是', p1)
p1.call()
print('可以看出，self就是\'当前对象\'本身，实质就是同一块内存地址')

print()
print('以下是另一部手机p2，它与p1有着不同的地址')
p2 = Phone()
print('当前对象的地址是', p2)
p2.call()  # 当对象p2调用普通方法时，就将对象自身作为参数self传递给了普通方法，也是为何self不用指定形参的原因
print('可以看出，self就是\'当前对象\'本身，实质就是同一块内存地址')

# p2.call()   当p2.的时候，就意味着p2已经有了自己的内存空间了，否则就.不出来东西
p2.price = 99999
print(p2.price)

# 类的魔术方法   魔术方法，能够在特定的时候自动触发，不需要调用
print()
print('类的魔术方法')


class Phone:
    # 魔术方法之一
    def __init__(self):
        self.brand = 'huawei'  # 动态地给self空间(对象空间)中添加了brand属性，保证了类生成的每个对象都有brand属性
        self.price = 4999
        print('我是类中定义的、一定会被执行的魔术方法__init__')

    def call(self):
        print(self.price)


p = Phone()  # 未调用类的方法就已经执行得到了print的结果：'我是类中定义的一定会被执行的魔术方法__init__'
# 1、找有没有一块类内存空间是Phone
# 2、如找到，那么利用Phone类向内存申请一块对象的内存空间
# 3、去类空间Phone中找有没有__init__,如果没有则将'对象'的内存空间地址赋给'对象名'p
# 4、如果类空间Phone中找到了__init__,则'对象'会进入init方法执行里面的动作，将'对象'自身的地址传给init方法的self参数
# 5、执行完了__init__，最后再将对象的内存地址赋值给'对象名'p
# 对Phone加()的理解，可以认为()就是一个调用，是Phone去调用__init__
# 一个思想，人看名，解释器看地址
print()
p.call()  # 可以看出p对象有了默认的price：4999
p.price = 5999
p.call()  # 可以修改p对象的属性price：5999

# 无论是def __init__(self):，还是def call(self):，定义时候都可以带参数

# 类方法和类属性
print()
print('类方法和类属性************')
print()


class Dog:
    leishuxing = '我是类属性'
    __leishuxing = '我是类的私有属性'   # __用来定义类的私有属性，类外部不能直接访问

    def __init__(self):
        self.nickname = '初始化狗'

    def run(self, nick):
        self.nick = nick
        print('{}在跑步'.format(self.nick))
        print()

    @classmethod
    def test(cls):  # cls是class的缩写，类方法以类作为参数
        print('类方法已经定义')
        print(cls)
        print(cls.leishuxing)  # 类方法只能调用类属性
        # cls是class的缩写，类方法以类作为参数，所以以下语句均报错
        # print(cls.nick)   nick是对象属性
        # print(self.nickname)   nickname同样是对象属性

    @classmethod
    def show_class_attribute(cls):
        print('这里打印的是类的私有属性__leishuxing：',cls.__leishuxing)
        print('#',Dog.__leishuxing) # 注意这里是直接通过类名访问的，没有用到cls

    @staticmethod  # 这是静态方法的定义方式
    def test_static():  # 不需要cls做为参数，其他的特性与类方法一摸一样，都只能访问类，不能访问对象
        print('直接通过Dog.__leishuxing来访问类属性',Dog.__leishuxing)


d = Dog()
print(d.nickname)
d.run('大黄')

Dog.test()
print('*',Dog.leishuxing)# 类属性可以直接得到，注意Dog类在print执行时直接就在内存中生成了，注释掉上5行也不影响本行结果
#print(Dog.__leishuxing)  # 私有的类属性，只能在类方法中被读取和修改，因此此句报错
Dog.show_class_attribute()  # 通过类方法来调用类的私有属性
Dog.test_static()
'''
类方法
特点：1、定义需要依赖装饰器
2、类方法的参数是一个类cls，不是对象self
3、类方法中只可以使用类属性
4、类方法中不能使用普通方法，因为普通方法是对象的

类方法的作用：类方法和类属性在类产生时就已经产生，此时对象还没有产生
因此类属性和类方法可以用来完成一些在对象创建之前就需要完成的一些功能

'''

print()
print('*' * 30)
print()




