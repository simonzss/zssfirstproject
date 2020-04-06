# 单例，是一种开发模式，即一个类只能创建一个对象，或者说，一个类无论创建多少次对象，这些对象的内存地址都只有一个

class Singleton:
    __instance=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

s1=Singleton()
s2=Singleton()
print(s1) #<__main__.Singleton object at 0x0000022EA2765D00>
print(s2) #<__main__.Singleton object at 0x0000022EA2765D00>
