# 闭包
# 闭包是函数的概念
# 闭包的条件 1、在外部函数中定义了内部函数
# 闭包的条件 2、外部函数中是有返回值的
# 闭包的条件 3、返回的值是内部函数名，不能加括号
# 闭包的条件 4、内部函数要引用了外部函数的变量值
# 闭包的作用 1、能够保存返回闭包时，外层函数变量的状态
def father_fun(a,b):
    c = 10
    def son_fun():
        print(a+b+c)  # 注意内部函数是引用了abc的
    return son_fun

# 当调用father_fun(1,2)--->a=1,b=2传入到son_fun()内部函数中--->返回内部函数(此时返回的内部函数已经记录此时a和b的值)
# 所以不会受到a,b改变的影响
father_fun(1,2)()


# 闭包的应用之计数器

def func():
    jishu_list=[0]
    def inner_func():
        jishu_list[0]=jishu_list[0]+1
        print('函数func()运行了第{}次'.format(jishu_list[0]))
    return inner_func

func()()      #特别注意这里,这里直接执行不用变量接收是实现不了闭包的
print(func())
func()()
func()()
print(func())
x=func()      #与上面的值是不同的,想要实现闭包必须用变量x来接收func()
x()
print(x)
x()
print(x)
x()
print(x)