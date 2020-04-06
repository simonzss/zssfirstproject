# 魔术方法之 __str__方法  注意这个方法只能返回'字符串'类型的值
# concatenate衔接，连接

# __str__方法  单纯打印对象名，得到的是内存地址，如果想要在打印对象名时得到更多的信息，就可以自定义__str__方法
# __str__方法中一定要有return，return后面的内容就是打印对象时看到的部分
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # __str__方法只能返回字符串类型
        # return '对象名：'+self.name,'年龄是：'+str(self.age) # 注意这句的写法是错的
        return '对象名：' + self.name + '年龄是：' + str(self.age)


p = Person('jack', 18)
print(p)

# 魔术方法的总结
# 重点 __init__   __str__
# 非重点  __new__  __del__  __call__(想不想将对象当函数用)


# 方法的总结
# 普通方法  对象调用
# 类方法  @classmethod    类调用、对象调用
# 静态方法   @staticmethod   类似于类方法，只不过不用明确的cls参数
# 魔术方法  无需调用，某些时刻自动执行

class A:
    def a(self):
        pass
    def b(self):
        self.a()   # 这是b方法调用a方法的用法
        pass
