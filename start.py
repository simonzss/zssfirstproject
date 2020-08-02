# invalid syntax 无效语法
# character 字符
# identifier  标识符|变量
# directory 目录(文件夹)
# C:\Python38\Lib\site-packages是pip安装的默认路径
# module builtins 内置模块
# append 追加
# truncated 删短
# indentation 缩进
# trailing跟随 newline  stripped脱光
# prompt提示
# operator 运算符|接线员
# identity 身份
# parsing 语法分析
# Unresolved   未解决的
# reference 参考、引用
# parameter  参数
# binary 二进制
# resolution 决议、决定
# 转义字符 \n 换行 \t 制表符   \'  \"
# \r 回车（打印头回到行首，如果没有与\n同用，会导致已有的内容被覆盖）
# r'任意字符串'  r=raw   原样不转义输出  但不能是print(r'\')
# '''任意字符串'''  三引号内的字符串保留格式输出（被赋值给变量时），也可做为注释使用（未被赋值给变量时）
# 占位符 %s 字符串  %d digit 整型|不保留小数点的数字    %f  float 四舍五入保留小数点的数字 %.2f 保留两位四舍五入小数
import keyword

print(keyword.kwlist)

a = 3
b = 4

print('hello')
print('world', type(a))
print('这里是a=%s,这里是b=%s' % (a, b))  # %s已经在底层进行了强制类型转换，将a从int强制转换为了str
print('我%d都是%s枪%s' % (18.5, '神', '手'))
print('我%.2f都是%s枪%s' % (18.566, '神', '手'))
print('我今年{}岁了，我喜欢{}'.format(2, '上幼儿园'))  # format是字符串的一个函数，‘.’表示调用
#  input()  只会接收字符串类型的输入，如果需要整型，需要int()
# print() 可以用来直接换行  用嵌套循环打印三角形时会用到

name = 100
name1 = 10 * 10
print(id('admin'))
print(id(name), name)
print(id(name1), name1)

# 赋值符号=   扩展后的赋值符号 +=  -=   *=  /=
# 运算符号+ - * /    扩展后的运算符号  **（高次幂）  //（除法取整）  %（除法取余数）
num = 10
num /= 3
print(num)
num = 8
print(8 ** (1 / 3))  # 高次幂用来做开方
print('*' * 50)  # 字符串的乘法

# 关系运算符  ==  !=   >=   <=  is(同样返回True或者，但可用于对象间的比较)
# 小整数对象池：Python对小整数的定义是 [-5, 256] 这些整数对象是提前建立好的，不会被垃圾回收


# 逻辑运算符  and  or  not

# 二进制   十进制  int()
# 计算机中的负数二进制是用正数的二进制进行反码（所有位01互变）再补码（最低位+1）后得来
print(bin(8))  # 0b1000   0b是二进制的表示  0o6430 0b是八进制的表示  0x6430 0x是十六进制表示
print(bin(10))  # 0b1010
print(bin(-10))
print(bin(15))
print(bin(16))
print(int(-0o6430))
print(~5)
print(3^5)
# 位运算  & 与  |或  ~非   ^异或（相同是0，不同是1）  <<左移 左移补0  >>右移 右移补运算符

#python的三目运算
a=5
b=6
result=(a+b) if a<b else (a-b)
result1=(a+b) if a>b else (a-b)
print(result)
print(result1)

#if  elif  elif   else
#for   else  当for里面的循环数‘为零’ 或者 ‘用尽’的时候，就会进入else分支
# break 用来提前跳出for循环的“整个”代码块   跳出循环时也会不执行for下的else（else属于for的一部分，会被break一并跳出）
# continue 不执行continue下方的循环体其他语句，直接进入下一次循环
print('*' * 20,'循环开始')
for i in range(5):    # 这里的range(5) 位置可以是任意的序列，例如可以写一个字符串，for循环将会把这个字符串每个字母遍历打印
    print(i)
else:
    print('循环结束')

# while实现累加
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(sum)

# while实现99乘法表
ceng=1
while ceng<=9:
    count=1
    while count<=ceng:
        print('{}*{}={}  '.format(count,ceng,(count*ceng)),end='')
        count+=1
    print()
    ceng+=1

#python 在for while循环中没有作用域一说，for while里面声明的变量在循环体外也可以拿到

# ==  与  is  的区别
s1='abc'
s2='abc'
# s3=input('请输入s3的值')  #输入'abc'
# s4=input('请输入s4的值')  #输入'abc'
print(s1==s2)
print(s1 is s2) # 这里是常量赋值，所以s1的地址等于s2的地址
#print(s3==s4)   # 值是True   说明  ==  比较的是值
# print(s3 is s4) # 值是 False 说明  is  比较的是内存地址   这里是input进来的值，所以地址不同

# 字符串支持 +   *   in    %s   %d   %f   %.2f   r(保留原格式)  切片操作[]  [:]与range()一样包前不包后  [::]
print('picture.png'[0:7])
print('picture.png'[0:-4])  #由左到右是01234，由右到左是-1-2-3-4
print('picture.png'[::-1])
print('picture.png'[8:11:1])
print('picture.png'[-1:-4:-1])
print('picture.png'[0:-1:2])
print('picture.png'[0::2])

# 字符串函数  find()  lfind()  rfind()  index() replace()  encode()编码  decode()解码
# 字符串函数  startswith()  endswith() 均返回布尔值
# 字符串函数  isalpha()   isdigit() join()   lstrip()   rstrip（）用来去除字符  split()切割 输出为数组
filename='文档.doc'
print('判断字符串尾部函数---->',filename.endswith('doc'))
print('_'.join('abc'))
print(''.join(['l','o','v','e']))   #[]为列表


# in的用法需要掌握  可用来判断字符是否在字符串里，列表元素是否在列表里等等
name_list = ['tom','jerry','bobby','cona']
print(name_list[1])
print('*************')
name_list1 =[]
# 列表支持切片操作[]
# 列表添加元素的方法  append()   extend()   insert(下标数字,添加内容)下标数字位置插入添加内容
# 列表删除元素的方法  del(list[index])    remove() 删除第一次找到的元素，返回None，找不到则抛出异常
# pop() 弹栈  默认从末尾删除，把删除掉的元素返回值  也可以传参指定弹出某一个下标的元素  弹栈相当于手机的返回键
# 列表是栈的一种表示   栈：后进先出   队列：先进先出 First In First Out
# clear()  清除所有元素
# reverse()  反转   sort()  排序    count()统计次数
name_list1.extend(name_list)
print(name_list1)
name_list1.extend('黑嘉嘉')
print(name_list1)

# iterable 可迭代的，可重复的   什么叫可迭代，能放入for循环的就是可迭代
# sorted()函数  ascending上升的  custom定制，惠顾
# 列表嵌套
print('--------------列表嵌套-------')
l1=[1,2,3,4]
l2=[1,2,3,4,[3]] #列表嵌套  l2列表是二维的
print(3 in l1)
print([3] in l1)
print([3] in l2)
print(l2[4])     #列表第一维访问，返回[3]
print(l2[4][0])  #列表的第二维访问 返回3

print(range(1,10,3))  #期待结果1，4，7,但打印结果为range(1, 10, 3)
print(list(range(1,10,3)))  #类型转换 list类型 ******只能转换可迭代对象******

print(list('abc'))  #字符串可以迭代iterable   结果为['a', 'b', 'c']
#print(list(10))  # 不能成功，因为整型是不可以迭代的，所以不能用list()转换

l=[0,1,2,3,4,5,6,7,8,9]
print(l[:5:-1])  #注意这一题
print(l[0:9:1])
print(l[::1])

# enumerate 枚举  返回下标和值两个东西，所以用index和value两个变量去接收
print('******枚举******')
for index in enumerate(l):
    print(index)

for index,value in enumerate(l):
    print(index,value)

# 排序核心思想  方法1（选择排序）：找出最小的放最左边，找出第二小的放左二...以此类推   方法2（冒泡排序）：找出最大的一个放最右边，找出第二大的放右二...以此类推
# 冒泡排序中用到的快速交换
a=3
b=4
a,b=b,a  #将a,b的值交换
print('a=',a)
print('b=',b)

# https://www.bilibili.com/video/av69060979?p=73  总结列表

#tuple 元组  元组内容不可修改
# 如果元组只有一个元素，那么不构成元组，即加不加括号都一样，如果是一个元素加逗号，便构成元组，例如  (1)不构成元组  (1,)构成元组
#因元组不可修改，故tuple()提供将现成的list转换为元组功能
# 元组查询 可通过下标index  可通过切片[:]
# 元组带的函数   count()   index(参数)找出值等于参数的第一个 元素的下标
y = (1,2,3,4,5,6,3)
print(y.index(3))
#元组的拆包
a,b,*c=y  # *代表通配符，结果为1 2 [3, 4, 5, 6, 3]        此时a的类型是int b的类型是int  而c的类型是list
print(a,b,c)
print(*c)   #给变量赋值时*代表封装，将3，4，5，6，3封装为列表      而给函数print赋值时*代表拆封，这是在传递实参，将[3,4,5,6,3]拆封为3,4,5,6,3

# 字典 {} 字典内的元素必须成对key:value   故强制转换函数dict()中的最基层元素必须成对出现
dic = {'name':11,'age':18,'id':19}
# 向字典中添加
dic['phone']=13555555555       # dic[key]=value    修改同样，同名key不同value进行替换，实现修改。  key在字典中是唯一的
print(dic)

# 列表的增删改查通过下标index完成，字典增删改查通过key完成，字典没有下标
# 字典函数  字典.items()   .keys()   .values()
# 直接遍历字典就会遍历key，所以有if name in dic：这种用法，因为name在key中，所以返回为True
# 字典取值函数dic.get(key[,default])  通过key取得value，如果找不到key则返回None，还可以设置如果找不到key则返回默认值
# 字典删除函数pop(key[,default])   通过key删除键值对，如果找到key，则返回删除的键值对的value     如果没找到key，可以通过default设置默认值，如'字典中无此键值对'
# popitem() 删除字典末尾的键值对    update()合并    fromkeys(seq[,default])将seq转换为字典,value值由default指定
# https://www.bilibili.com/video/av69060979?p=82   seq回顾

for key,value in dic.items():
    #print(type(value))
    if value>15:       #value和key始终一一对应成对出现
        print(key)

print('*****************************************')
print(dic.items())

# 集合  set   无序 互异 确定性       定义同样使用{},如果里面是键值对，是字典，如果里面是元素，是集合
# set的函数  add()增加一个元素，元素不拆包   update()将元素拆包加到set里   discard()删除
# set 的- 差集  difference()  &交集  intersection   |并集 union()
# set中^的用法  对称差集    相当于(s1|s2) - (s1 & s2)
print('*****************************************')
s1={1,2,3,4,5}
s2={2,3,4,5,6,7}
s1.difference(s2)
print(s1)
print(s1.difference(s2))
print(s1)
s1.difference_update(s2)  #注意此函数的意思 差集并且重新赋值s1的值               此函数返回值为None，故直接打印出来结果为None
print(s1)


# 可变类型与不可变类型  https://www.bilibili.com/video/av69060979?p=86  指的是  对象所指向内存中的值是否可变
# 不可变类型  int float str turple
# 可变类型  list  dict  set  其中set可以通过frozenset()转变为不可变类型






