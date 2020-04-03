# 可迭代的对象  1、生成器  2、元组、列表、集合、字典、字符串
# 如何判断一个对象是否是可迭代
from collections.abc import Iterable

list1=[1,2,3,4,5]
g=isinstance(list1,Iterable)
print(g)


# 可迭代 Iterable
# 迭代器 Iterator  迭代器只能往前不能后退
# 两者有区别
# 可迭代，即用isinstance(X,Iterable)判断为True的对象，如列表
# 迭代器，则是可以用next()方法不断取得内部值的对象，列表就不是迭代器
# next(list1) 就是错误的，会报错TypeError: 'list' object is not an iterator
# 列表是可迭代的，但不是迭代器。生成器是可迭代的，也是迭代器
# 可以用Iter()方法将可迭代的转化为迭代器
# 迭代器是一个大的范围，包括生成器，'list_iterator'，'tuple_iterator'
# 迭代器分为两大类，一大类是生成器，不需要iter()转换直接用next()
# 另一大类是要借助于iter()转换才能应用next()，例如'list_iterator'，'tuple_iterator'
print()
print('将列表转化为迭代器')
g=iter(list1)
print(type(g))
print(next(g))
print(next(g))