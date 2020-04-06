
class Student:
    def __init__(self,age):
        self.__age=age

    @property
    def agee(self):
        return self.__age
    @agee.setter
    def agee(self,x):
        self.__age=x


s=Student(5)
print(s.agee)  # 这是通过agee方法来给__age赋值和取值
s.agee=10
print(s.agee)

# ######################################################
'''
class Student(Person):下没有任何实质性代码
注意Person类的super_clazz_salary,__super_clazz_salary,self.__money,self.salary这四个属性
这四个属性都能被Student的对象继承，在s.__dir__()中是同一个命名空间内的，只不过是加了__的换了名字(伪私有)
'''
class Person:
    super_clazz_salary=500
    __super_clazz_salary=10000
    def __init__(self):
        self.__money=100
        self.salary=555

    def hello(self):   # 类方法必须定义返回值，否则默认返回None
       return 'hello'

    def hello1(self):   # 类方法必须定义返回值，否则默认返回None
       print('hello')

class Student(Person):
    pass


s=Student()
print(s.__dir__())
print()
print(s.hello())
print()
print(s.hello1())
#print(s.salary)

#print(s.super_clazz_salary)
print(s.salary)

#  几种继承时super的用法
'''
super().__init__()               # 注意super是一个系统类，super()是一个对象，对象.__init__()会默认把对象传入()内作为参数
super(Person, self).__init__()   # 故()内不用再加self作为形参
Person.__init__(self)            # 而Person是一个类，类调用自身的方法就需要()内传入对象，故要写明self作为形参
'''
# 超类构造函数  就是__init__