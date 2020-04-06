# 类的多继承顺序
# Python 3 中，多继承顺序统一为'广度优先'

class A:
    def foo(self):
        print('A的foo方法')

class B1(A):
    def foo(self):
        print('B1的foo方法')

class B2(A):
    def foo(self):
        print('B2的foo方法')

class C1(B1,B2):
    def foo(self):
        print('C1的foo方法')

class C2(B1,B2):
    def foo(self):
        print('C2的foo方法')

class D(C2,C1,A):   # 注意这里的写法，C1与C2谁在前就先找谁,广度优先，爸爸们找完再找爷爷们
    pass            # 可以把爷爷辈的A写进去，写不写A效果一样

print(D.__mro__)
import inspect
print(inspect.getmro(D))   # mro method resolution order 方法决议顺序

d=D()
d.foo()


# Phthon 2 里多继承还存在着 '从左至右，深度优先'的顺序，已经变成了时代的眼泪
# 即先找第一个爸爸，然后向上找第一个爸爸的从左到右的爷爷们，再向上找直到Object
# 如果没找到，再回来找第二个爸爸，以及第二个爸爸的爷爷们，再向上找直到Object，没找到的话再回来找第三个爸爸...以此类推


# 面向对象三大特征   多态  封装  继承
# 封装即私有化    继承 has a 和 is a
# 多态  即允许接受父类的地方，同样也允许接收父类的子类,多态始终强调类的继承
# 多态  不同的子类对象调用相同的父类方法，产生不同的执行结果，可以增加代码的外部调用灵活度，
# 强类型语言中，规定类型的地方如果接收其他类型会直接报错
# Python中，如果要限制只能接收某一个类型，需要用if语句
'''
多态始终强调类的继承，而Python的鸭子模型并不关注是否继承，只关注是否有符合要求的"方法和属性的集合"
所以我们说， Python不支持多态，也不用支持多态，python是一种多态语言，崇尚鸭子类型
在鸭子模型中，一个对象是否可用不再由继承特定类或实现特定接口实现，而是由它有的"方法和属性的集合"决定。
鸭子模型的简单灵活，甚至会让我们没有意识到python中有多态。 这是动态语言的优点，但也是动态语言的缺点。
优点是，通过这个特性，我们省去了繁杂的继承关系，同时实现很多静态语言无法实现的高级用法，加快了开发的效率。
缺点是，过于灵活的语言就必然会增加出错的概率，不便于后期的维护。
在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的
'''
print()
print('以下为无多态代码')
print()


class ArmyDog(object):
    def bite_enemy(self):
        print('追击敌人')


class DrugDog(object):
    def track_drug(self):
        print('追查毒品')


class Person(object):
    def work_with_army(self, dog):
        dog.bite_enemy()

    def work_with_drug(self, dog):
        dog.track_drug()


p = Person()
p.work_with_army(ArmyDog())
p.work_with_drug(DrugDog())


print()
print('以下为多态代码')
print()


class Dog(object):
    def work(self):
        print('和狗一起工作')


class ArmyDog(Dog):
    def work(self):
        super().work()
        print('和军犬一起追击敌人')


class DrugDog(Dog):
    def work(self):
        print('和缉毒犬一起追查毒品')


class Tiger:
    def work(self):
        print('和老虎一起工作')




class Person(object):
    def work_with_dog(self, dog):  # 只要能接收父类对象，就能接收子类对象。前提是子类对象拥有work()方法就行
        dog.work()                 # 不同子类会产生不同的执行效果。


class Person_Fear_Tiger:
    def work_with_dog(self, dog):
        if isinstance(dog,Dog):
            dog.work()
        else:
            print('和我工作的不是一只狗，我怕怕~~')


p = Person()
p.work_with_dog(Dog())
print()
p.work_with_dog(ArmyDog())
print()
p.work_with_dog(DrugDog())
print()
p.work_with_dog(Tiger())   # 注意，Tiger并不继承于Dog,只要Tiger定义有work()方法，就可以被p.work_with_dog调用
print('*********************')
p1=Person_Fear_Tiger()
p1.work_with_dog(Tiger())
p1.work_with_dog(ArmyDog())