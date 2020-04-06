'''
私有化   私有化属性的访问仅限于 '类'中，例如，__name__属性可以被类中定义的各个方法直接使用
但出了类就不能被直接访问到，比如由类生成的对象，就无法直接访问到私有化属性，只能通过get和set方法访问
'''
# 封装  1、具有私有化属性   2、定义公有的get和set方法
# 好处  1、隐藏属性不被外界随意修改
#      2、如果需要修改，要通过set函数，set函数是类里定义的，对象天然具备的。set函数里面可以设置约束条件。
#      3、如果需要获取某一个私有化的属性，要通过get函数，get函数必须有返回值

class Student:

    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def setScore(self, score):
        self.__score = score

    def getScore(self):
        return self.__score

    def __str__(self):  # 注意__str__方法只能返回字符串  必须用return 而不是print
        return '{}的年龄是{}岁，分数是{}'.format(self.__name,str(self.__age),str(self.__score))

xiaoming=Student('xiaoming',18,59)
print('通过get方法得到小明的分数',xiaoming.getScore())
print(xiaoming)
xiaoming.setScore(95)
print('通过get方法得到小明的分数',xiaoming.getScore())

print()
print(dir(Student))  # 无法看到__score
print()
print(dir(xiaoming)) # 同样无法看到__score,有_Student__score，但同样无法访问
print(xiaoming.__dir__()) # 和上一句作用是一致的

'''
python的私有化是伪装的私有化
通过dir(xiaoming)查看attribute后，看出存在_Student__age，它实际就是__age
python通过将__age  改名  为_Student__age，实现了无法直接访问xiaoming.__age
但对象xiaoming可以直接访问改名后的_Student__age
所以是伪装的私有
'''
#print(xiaoming.__name) #AttributeError: 'Student' object has no attribute '__name'
print(xiaoming._Student__name)
print(xiaoming._Student__age)
print(xiaoming._Student__score)


# comprising 包括
# attributes 属性
# parameter翻译成“形式参数”，把argument翻译为“实际参数”  <---   来自网络，准确性待查
# 即把attribute按照常规翻译为“属性”，把property翻译为“属性式函数”或“属性函数” <---  来自网络，准确性待查
# 对象xiaoming里的__init__ setScore getScore __str__ 统统叫做attribute
# 类里定义的函数，也都统称为attribute
# attribute范围大，property范围小，attribute包括了property  <---  来自网络，准确性待查

print(__name__)  # "__name__"内置函数出场了~！
'''
__name__ 记录着一个字符串：1、当前执行的程序调用__name__ ，返回的字符串是" __main__ "；
　　　　　　　　　　　　　　 2、如果是被其它文件导入，__name__ 返回的字符串则是导入文件的文件名。
因此有了
def say_hello():
    print("hello world")

if __name__ == "__main__":    # 这就确保了如果被其他文件导入，就不会执行if内部的语句
    print(__name__)
    print("这是测试模块1")
    say_hello()

'''

###############################################################################
print()
print('装饰器用来定义set和get方法')
print()

class Student1:

    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    # def setScore(self, score):
    #     self.__score = score
    @property
    def score(self):  # 注意这里直接用一个score函数，加上不同的装饰器就实现了get和set，不再用getScore和setScore
        return self.__score

    @score.setter     # 必须先get再set，因为set依赖get
    def score(self,score):
        self.__score=score

    def __str__(self):  # 注意__str__方法只能返回字符串  必须用return 而不是print
        return '{}的年龄是{}岁，分数是{}'.format(self.__name,str(self.__age),str(self.__score))

xiaohua=Student1('xiaohua',18,99)
print(xiaohua.score)
xiaohua.score=88
print(xiaohua.score)