import random


def generate_random(numm):  # 形参  形式上的参数     n这个参数就相当于在函数内存地址上开的一个口子，这个口子必须依赖外界来的值
    for i in range(numm):
        print('这是函数内的n--->%d2' % id(numm))
        num = random.randint(1, 20)
        print(num)


# numm = int(input('请输入循环次数：'))
# print('这是函数外的n--->%s' % id(numm))
# generate_random(numm)  # 实参  实际的参数，具体的值

# 判断是不是什么类型  不能用type，应该用isinstance() 返回布尔类型值
print(isinstance(2, int))


# 赋值的核心就是赋内存地址

# 可变参数 args=arguments 多个参数
def kebian(*args):  # 定义函数时，*的机制是直接将*封装为一个空的元组，然后看args里面有东西就往元组里填，没有就保持空元组
    print(*args)


kebian()  # 机制是直接将*封装为一个空的元组，然后看args里面有东西就往元组里填，没有就保持空元组
kebian(1)  # 封装为(1,) 如果元组只有一个元素，那么不构成元组，即加不加括号都一样，如果是一个元素加逗号，便构成元组，
# 例如  (1)不构成元组  (1,)构成元组
kebian(1, 2)


# a,*b=1,3,4,5,6   则封装为 a=1  b=(3,4,5,6)
# 如果可变参数与不可变参数并存，则可变参数必须放在不可变参数的后面  def kebian(name,*args)

# 关键字参数 key=value  默认值参数
# 例如 def gjzcs(a,b=10):  b=10就叫做关键字参数，10是一个默认值，可以传入别的值
# 多个关键字参数
def gjzcs1(a, b=10, c=20):
    print(a + b + c)


gjzcs1(10)  # 结果是40
gjzcs1(10, c=10)  # 结果是30  通过关键字的key指定给c这个变量赋值


# 可变关键字参数**kwargs   kew word arguments
def keyw(**kwargs):
    print(kwargs)


keyw(a=1, b=2, c=3)  # 封装为了字典  输出{'a': 1, 'b': 2, 'c': 3}
keyw()  # 可变关键字   输出{}

# 可变参数 定义函数时，* 的机制是直接将*封装为一个空的元组，然后看args里面有东西就往元组里填，没有就保持空元组
# 可变关键字参数 定义函数时，** 的机制是直接将**封装为一个空的字典，然后要求args里面的东西必须是key=value的形式，才能往字典里填，没有就保持空字典
dic1 = {'1': 'python', '2': 'java', '3': 'c++', '4': 'golang'}
# keyw(dic1)  直接将字典传入是错误的，因为**kwargs要求的是key=value，不能把字典再封装为字典
keyw(**dic1)  # 此处逻辑是，第一步将字典dic1拆包为key=value形式，既keyw(‘1’=python,'2'='java','3'='c++','4'='golang')
# 第二步将这些key=value再封装为字典

# 给变量赋值时*代表封装，将3，4，5，6，3封装为列表
# 而给函数print赋值时*代表拆封，注意这里不是在定义函数，而是在调用函数，是在传递实参，故*代表拆封，将[3,4,5,6,3]拆封为3,4,5,6,3
# 定义函数时，()的*和**代表封装    调用函数时，()内的*和**代表拆封
a, b, *c = (1, 2, 3, 4, 5, 6, 3)
print(a, b, c)  # 注意这行打印出c的值为[3, 4, 5, 6, 3]
print(*c)  # 注意这行打印结果并不是[3, 4, 5, 6, 3]，而是3，4，5，6，3


def demo(a, b, *c, **d):
    print(a, b, c, d)


demo(1, 2)  # 输出1 2 () {}
demo(1, 2, 3, x=1)  # 输出1 2 (3,) {'x': 1}  注意元组单元素必带逗号

print('________________________________')


def a(b, bb=20):
    print(b, bb)
    return b, bb   # 返回值可以有多个


a(b='hello')
a('hello')
a('hello', 40)
print('________________________________')
x = a('hello')  # 用一个变量接收返回值，则return将返回值封装为元组
print(x)
x, y = a('hello')  # 用多个变量接收返回值，则return分别将返回值赋给变量
print(x, y)
# 当一个函数没有返回值时，如果用一个变量去接收函数，则这个变量只能接收到None


# 嵌套调用  即函数间的调用  一个函数内部可以去调用另一个函数
# 全局变量和局部变量  函数外定义的叫全局变量，函数内可以直接查询读取，函数内定义的叫局部变量，不能被另一个函数查询读取
# 函数体内部不能改变'不可变全局变量'的值，如果改变，需要在函数体内第一行声明    global 全局变量   才可在函数内部修改全局变量的值
# 函数体内部可以直接改变'可变全局变量'的值  如list等
# 内部函数与nonlocal

intout=999
def father():
    int1=100   # 256之内的小整数，不可变
    list1=[1,2,3,4,5]
    def son():
        nonlocal int1  # 内部函数想修改外部函数的不可变值，就要加nonlocal，而可变值list1就可以直接修改
        global intout  # 内部函数想修改全局的不可变变量，需要在内部函数第一行加global
        for index,value in enumerate(list1):
            list1[index]=value+int1
            print(list1)
        int1+=100
        intout+=1
        print('son()里面的locals是:',end='')
        print(locals())    #注意内置函数locals()的用法，查看’局部‘声明的内容有哪些，因’局部‘位置不同，而结果不同，这里是属于son()
    son()  #内置函数定义完后必须要调用才能起作用
    print('father()里面的locals是:',end='')
    print(locals())        #注意内置函数locals()的用法，位置不同，结果不同，这里是属于father()
    print(int1)
    print(intout)
father()
print(globals())  #这句放哪都一样，只有一个全局变量字典


