# 作用域  LEGB规则
# L Local
# E Enclosing  嵌套
# G Global
# B Built-in  内置的

a=100

def func():
    a=10

    def inner_func():
        a=1
        print(a)
        print(max)   # 内置的  并未在本文件中定义
    inner_func()

func()