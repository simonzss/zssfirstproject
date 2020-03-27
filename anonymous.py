# 匿名函数
from _collections_abc import Iterable
from functools import reduce

s = lambda a, b: a + b
print(s)

result = s(1, 2)
print(result)

print('*******匿名函数作为参数*******')


# 匿名函数可以作为函数的参数
def add(a, b, func):
    print(func)
    s = func(a, b)
    print(s)


add(1, 2, lambda a, b: a + b)  # 1，2，与lambda a,b:a+b 是平等地位，lambda a,b:a+b直接引用了a和b

# 匿名函数在内置函数中的应用
print('**********匿名函数在内置函数中的应用*************')
list1 = [{'a': 10, 'b': 10}, {'a': 11, 'b': 20}, {'a': 12, 'b': 30}, {'a': 13, 'b': 44}]
# 下一句暂时理解为调用函数时发生了参数解包，即将list1先进行解包，将解包后的结果再传给函数参数，即*[, key=func]
r = max(list1, key=lambda x: x['b'])  # 注意，max是系统内置函数，默认会‘一个一个’拿出元素进行对比，而list1的元素就是字典，
print(r)  # 因此max函数将一个一个的字典传给lambda函数去执行，并拿到返回值作为比较的key
print(isinstance(list1, Iterable))  # 可以用isinstance来判断是否属于可迭代对象

# map函数
print('___________试用map函数____________')
list2 = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x + 2, list2)))
# 预备知识
re = lambda x: x if x % 2 == 0 else x + 1
print(re(6))
# map中的应用
re2 = map(lambda x: x if x % 2 == 0 else x + 1, list2)  # 实现了只针对于奇数的操作
print(list(re2))

# reduce函数
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
list3 = [2, 4, 6, 8, 10, 12]
print(reduce(lambda x, y: x + y, tuple1))
print(reduce(lambda x, y: x - y, list3))
tuple2 = (1,)  # 如果只有单个元素
print(reduce(lambda x, y: x + y, tuple2, 10))  # 则可以指定参与运算的第二个元素的值，默认为空

print(reduce(lambda x, y: x - y, tuple2, 10))  # 注意指定默认值时，减法的顺序

# filter函数
list1 = [{'a': 10, 'b': 10}, {'a': 11, 'b': 20}, {'a': 12, 'b': 30}, {'a': 13, 'b': 44}]
b = filter(lambda x: x['b'] > 20, list1)  # filter直接操作了list1中的items，注意filter的函数定义直接出现了items
print(list(b))  # 而max的函数定义中则没有出现items
'''
def max(*args, key=None): # known special case of max
    """
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
    """
    
    
class filter(object):
    """
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
'''

# sorted函数
print('---------sorted函数--------')
list1 = [{'a': 10, 'b': 10}, {'a': 11, 'b': 20}, {'a': 12, 'b': 30}, {'a': 13, 'b': 44}]
dict2 = {'a': 100, 'b': 20, 'c': 30}
bb = sorted(list1, key=lambda x: x['b'], reverse=True)
cc = sorted(dict2.items(), key=lambda x: x[1], reverse=True)  # 注意x[1]的用法
print(bb)
print(cc)
print(type(dict2.items()))  # items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回


# 递归函数  recursion   递归函数就是自己调用自己的函数，需要有入口，有出口，无出口就会变成死循环
print('--------递归函数---------')
def sum1(n):
    if n == 0:
        return 0
    else:
        return n + sum1(n - 1)
print(sum1(100))



