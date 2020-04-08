# 系统模块 中的sys模块

import sys
print(sys.path)
print(sys.version)
print(sys.argv)  # 运行程序时的参数，argv是一个列表

# 涨姿势：可以在资源管理器窗口地址栏直接输入cmd，cmd窗口就会默认切换到当前地址！！！
# 在项目start文件夹的cmd中执行python sousuolujing.py 100 200 300，就是把100 200 300 这三个参数传给了suosuolujing.py
# 此时的print(sys.argv) --->  ['sousuolujing.py', '100', '200', '300']
# 也可以在pycharm中点击右上角执行按钮左边的下拉菜单，点Edit Configurations,在Parameters栏里填入参数，一样的效果


# 系统模块 中的 time模块
import time
print(time.time()) # 生成当前的时间戳
time.sleep(0.5)
print(time.time()) # 两个时间戳有区别了

# 将时间戳转成字符串 time.ctime(时间戳)
shijianchuo=time.time()
print('当前的时间戳是',shijianchuo)
s=time.ctime(shijianchuo)
print('当前的时间戳转化为字符串是',s)
# 将时间戳转成元组 time.localtime(时间戳)
y=time.localtime(shijianchuo)
print(y)
print(y.tm_year,y.tm_mon,y.tm_mday,y.tm_yday)  # 元组里的元素可以调用
# 将元组转回时间戳 time.mktime(元组)
print(time.mktime(y))
# 将元组转成特定格式的字符串 time.strftime('自定格式字符串'[, tuple])
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 打印出当前时间的格式化字符串
# 将字符串转换为时间元组  time.strptime(string, '格式定义')
print(time.strptime('1980/07!09','%Y/%m!%d'))

#############################################

# datetime模块    time模块的升级版
# datetime模块：time 时间  date 日期  datetime 日期时间  timedelta 时间差

import datetime    # datetime都是基于对象的
print(datetime.time.hour)  # <attribute 'hour' of 'datetime.time' objects> 'datetime.time'对象的属性

d=datetime.date(1980,7,9)  # 创建date对象
print(isinstance(d,datetime.date))
# isinstance(a,A)  Return whether an object is an instance of a class or of a subclass thereof.
print(d.month)
print(datetime.date.ctime(d))   # 将对象转换为字符串

# datetime  timedelta
print(datetime.date.today())  # 注意today是类方法，有装饰器 @classmethod

now=datetime.datetime.now()
print('现在时间是',now)
timedelta=datetime.timedelta(hours=2)
now_before_two_hour=now-timedelta
print('现在时间的两个小时前的时间是',now_before_two_hour)

# 时间差的用途  数据redis 作为缓存 redis.set(key,value,时间差) 设置在时间差后自动销毁
# 会话：session  实质就是在内存中的缓存，时间差用来设定内存中存在的时间，超时就被内存回收