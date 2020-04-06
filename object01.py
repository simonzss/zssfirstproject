# 类 对象
# 将对象与现实中的事物对等，将一系列对象的共同之处抽象出来形成类
# 对象的特征抽象为类的属性，如手机的品牌，价格，屏幕大小
# 对象的动作抽象为类的方法，如打电话，发短信，打游戏


class Phone(object):  # 类的标准声明方法，所有类继承自object类，也可省略
    pinpai = 'huawei'  # '类属性'
    pass


class Phone1:  # 类的省略声明方法
    pass


print('打印Phone的结果是：', Phone)  # 这时内存里已经有了类的地址
print('打印Phone的内存地址是：', id(Phone))  # 这时内存里已经有了类的地址
s1 = Phone()  # 使用类，创建对象
s2 = Phone()
print('打印对象s1',s1)  # <__main__.Phone object at 0x000001C52F497400>
print('打印对象s2',s2)  # <__main__.Phone object at 0x000001C52F4686D0>
print('对象s1的pinpai',s1.pinpai)  # 继承的类属性
print('对象s2的pinpai',s2.pinpai)
s1.pinpai = 'Iphone'  # 自定义动态创建的'对象属性'
print(s1.pinpai)  # 调用的时候先调用对象属性，如果'找到'就不再向上找类属性，如果'找不到'就在类属性里找，再找不到就报错
# 注意，对象不会在对象内存地址中复制类中的属性，而是用的时候去类的内存地址中调取。是指针机制。

s1.jiage = 5000  # 可以添加或者修改对象属性
print('给s1对象添加了类没有的jiage属性',s1.jiage)
print()
# 修改类属性
Phone.pinpai = 'xiaomi'
print('将类的pinpai属性修改为:',Phone.pinpai)
Phone.jiage = 1  # 可以添加类属性
print('将类的jiage属性修改为:',Phone.jiage)
print('s2对象继承自类的pinpai属性是:',s2.pinpai)
print('s2对象继承自类的jiage属性为:',s2.jiage)  # Unresolved attribute reference 未解决的 属性 引用
