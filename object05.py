# 继承 has a   一个类中使用了另外一个自定义的类型   比如Student使用了Computer
# 类的自定义类型


class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def online(self):
        print('使用价格为{}，品牌为{}的电脑开始上网'.format(self.price, self.brand))


class Book:
    def __init__(self, book_name, auther, num):
        self.book_name = book_name
        self.auther = auther
        self.num = num

    def __str__(self):
        return self.book_name + '---作者' + self.auther + '---' + str(self.num) + '本'


class Student:
    def __init__(self, stu_name, computer):  # 这里直接把电脑写死，为了说明电脑的类型问题
        self.stu_name = stu_name
        self.books = []
        self.computer = computer

    def show_book(self):
        if not self.books:  # 列表为空的判断方法！！！if self.books == 不起作用
            print('{}现在一本书也没有'.format(self.stu_name))
        else:
            print('{}现在有下列书'.format(self.stu_name))
        for i in self.books:
            print(i)

    def borrow_book(self, book):
        self.books.append(book)
        print('借书成功,借的书是{}'.format(book.book_name))

    def __str__(self):
        l = ''
        for i in self.books:
            l = l + i.book_name + ','
        return self.stu_name + '拥有这些书：' + l + '还拥有电脑' + str(self.computer)  # 此句的输出结果为
    # xiaoming拥有这些书：盗墓笔记,鬼吹灯,还拥有电脑<__main__.Computer object at 0x00000136FF38FD90>
    # 注意，computer的类型是Computer，Computer类型，自定义类型，即Computer1是Computer类型的对象


# 因为Student类使用了book类，所以要先生成book对象，在生成student对象
book1 = Book('盗墓笔记', '南派三叔', 10)
book2 = Book('鬼吹灯', '天下罢唱', 5)
computer1 = Computer('huawei', 4999)
print(computer1)  # 此句打印computer1对象，来确认computer1对象的类型
print()
print('***************')

xiaoming = Student('xiaoming', computer1)
xiaoming.show_book()
xiaoming.borrow_book(book1)
xiaoming.show_book()
xiaoming.borrow_book(book2)
xiaoming.show_book()
print(xiaoming)

######################################################################

# 继承 is a
# 子类继承父类，目的是在父类中定义所有子类的公共部分代码，提高代码的可读性和复用性

print()
print('继承的is a部分*********************************')
print()


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('{}在跑步,这是父类的跑步方法'.format(self.name))

    def __str__(self):
        msg = '姓名是{},年龄是{}岁'.format(self.name, self.age)
        return msg


class Student(Person):
    def __init__(self, name, age, clazz):  # 注意这里传参要传全，父类的参数要写，子类自己的参数也要写
        super().__init__(name, age)        # 写父类的参数name和age
        self.clazz = clazz                 # 写子类自己的参数clazz
        # 不能因为父类有__init__就不在子类里引入父类的__init__，否则子类的__init__会完全覆盖父类的__init__

    def readbook(self):
        print('{}班的{}在读书'.format(self.clazz, self.name))


class Employee(Person):
    def run(self):
        super().run()  # 这里首先通过super调用了父类的跑步方法
        print('这是子类自己定义的跑步方法，{}在跑步'.format(self.name))  # 然后再调用自己的跑步方法


class Doctor(Person):
    pass


s = Student('tom', 18, '初三二班')
print(s.name, s.age, s.clazz)

# 父类的英文名是 super class
# 当子类重写父类的方法时，叫做override 重写、覆盖，解释器就会只调子类方法，无论成功失败都不会再往上调取父类方法了
# 子类可以通过super().方法名(参数)  来调用父类的同名方法
e = Employee('jerry', 11)
e.run()
print(e)

# __str__里以下两种写法的区别
# 1、return self.stu_name+'拥有这些书：'+l+'还拥有电脑'+str(self.computer) # 此句的输出结果为
# 2、msg='姓名是{},年龄是{}岁'.format(self.name,self.age)
# 第1种写法，必须保证+号拼接的每一个部分都是字符串类型，所以用到str函数
# 第2种写法，直接用字符串的格式化写法，保证了msg一定是字符串

'''
同一个类中，如果定义同名但不同参数的方法，后面的方法一定会覆盖前面的
同一个类中，解释器不会因为参数不同就允许同名方法存在

'''


class A:
    def eat(self):
        print('无参数只管吃')  # 这个eat方法一定会被覆盖

    def eat(self, food):
        print('吃了{}食物'.format(food))


print()
a = A()
a.eat('大猪头')
