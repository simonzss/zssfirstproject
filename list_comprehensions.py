# list comprehensions 列表推导式
# 注意，列表推导式，所以得出的结果一定是一个列表
# [表达式 for 变量 in 旧列表 if 条件]
# [表达式 if...else... for 变量 in 旧列表 ]

# 过滤掉长度小于等于3的人名
list1 = ['tom', 'jerry', 'lucy', 'simon', 'lily', 'luna', 'sun']
list1_com = [x.capitalize() for x in list1 if len(x) <= 3]
print(list1_com)

# 将0-100之间能被3整除的数形成一个列表
list1_com = [x for x in range(101) if x % 5 == 0]  # range()包前不包后
print(list1_com)

# [(偶数，奇数),(),(),(),(),()]
list1_com = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]  # 这是for if for if层层包含(缩进)
print(list1_com)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [4, 7, 9, 5]]  # ----->[3,6,9,5]
list1_com = [x[-1] for x in list1]
print(list1_com)

# 列表中的字典
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'jerry', 'salary': 6000}
dict3 = {'name': 'lucy', 'salary': 4000}
dict4 = {'name': 'kona', 'salary': 3000}
list1 = [dict1, dict2, dict3, dict4]
list1_com = [x['salary'] + 1000 if x['salary'] > 5000 else x['salary'] + 2000 for x in list1]
list1_com2 = [{'name': x['name'], 'salary': x['salary'] + 1000} if x['salary'] > 5000
              else {'name': x['name'], 'salary': x['salary'] + 2000} for x in list1]
print(list1_com)
print(list1_com2)
# print(dict1.items())
# print(type(dict1.items()))
# print(isinstance(dict1.items(),list))
# print(list1[0].keys())

# 有列表推导式，也就有集合推导式，字典推导式
# 集合推导式，可以用来去重
# 以下为字典推导式的例子，注意字典的key要求是唯一的
dict1 = {'name': 'tom', 'salary': 5000,'wage':5000}    # 注意这里key和value交换后，key的唯一性问题，导致value被覆盖
dict1_exchange={value:key for key,value in dict1.items()}  # value的'salary'被覆盖为'wage'
print(dict1_exchange)