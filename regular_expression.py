# 正则表达式
# 正则表达式是用来在大量字符中匹配（寻找）符合自身字符规则的字符串，其实质就是一种过滤的规则
# python中就要用到re模块

import re

msg = '娜扎热巴佟丽娅'
msg1 = '佟丽娅娜扎热巴'

pattern = re.compile('佟丽娅')  # pattern对象
res = pattern.match(msg)  # pattern对象有很多方法，match是其中之一
print(res)
res = pattern.match(msg1)
print(res)

# 使用正则re模块的方法match，会直接将上述pattern过程封装
print('*******************')
s = '佟丽娅娜扎热巴'
result = re.match('佟丽娅', s)  # re.match('要找什么',在哪里找)
print(result)

# match是头部匹配，如果全文匹配，用search，但search只要找到就不再继续找下一个了
result = re.search('佟丽娅', msg)  # msg='娜扎热巴佟丽娅'
print(result)
print(result.span())  # 用span()返回找到的位置
print(result.group())  # 用group()返回找到的内容

# 正则中的[]    []中的任意一个字符匹配
s = '哈哈5'
result = re.search('[0-9]', s)  # 即0-9中的任意一个字符在s中匹配
print(result)  # <re.Match object; span=(2, 3), match='5'>  即5匹配上了
result = re.search('[0-4]', s)
print(result)  # 返回None，即0-4中任意一个都匹配不上5

s = 'sdahfu5ahdufa8haidsf9af'
result = re.search('[a-z][0-9][a-z]', s)  # 找出类似a0a的值
print(result)  # <re.Match object; span=(5, 8), match='u5a'>

# 全文匹配并找出所有用findall
s = 'sdahfu5ahdufa8haidsf9af'
result = re.findall('[a-z][0-9][a-z]', s)  # 找出'所有'类似a0a的值
print(result)  # ['u5a', 'a8h', 'f9a'] 把找到的全部放进一个列表里

# 找出a1a,a11a,a111a,中间任意个数字
# 个数：
# * 将前面的模式匹配>=0次  + 将前面的模式匹配>=1次 ? 将前面的模式匹配0次或1次
s = 'a1gfhjfgja11aasdgada111asdga1111absdfaa1m'
result = re.findall('[a-z][0-9]+[a-z]', s)
print(result)

# ^ $ {} 的用法 ^限定开头,$限定结尾,{}指定匹配次数，{m,n}即最小匹配m次，最大匹配n次。{m,}即大于等于m次
# 验证qq号码，必须是5-9位，首位不能为零
qq = '123456789'
result = re.match('[1-9][0-9]{4}', qq)  # <re.Match object; span=(0, 5), match='12345'>
print(result)  # 注意这个结果，它没有指定结尾，所以超过5位的依然能够匹配上。这是'部分匹配'
result = re.match('^[1-9][0-9]{4}$', qq)  # 用^限定从头开找，用$限定严格结尾，即必须'整体匹配'
print(result)  # 返回None
result = re.match('^[1-9][0-9]{4,8}$', qq)  # 实现了需求
print(result)

# 强调^和$的作用
# 用户名的验证，可以是字母或者数字，不能数字开头，长度6位以上。注意[a-z0-9A-Z]的写法包括了允许的所有值的范围
username = 'admin001#$'
result = re.match('[a-zA-Z][a-z0-9A-Z]{5,}', username)  # 注意用户名里出现了特殊符号，依然被匹配了
print(result)
result = re.match('[a-zA-Z][a-z0-9A-Z]{5,}$', username)  # 这就是$限定结尾的重要作用，^限定开头同理
print(result)  # match默认严格限定从头开找，而research不是，^对research就很重要了

# 进一步的简写 [a-z0-9A-Z_]==\w  即字母数字下划线   \w是正则的预定义
msg = 'aa#py bb.py ccc.py python  adfapythonsaf'  # 需要用到\b，正则中的\b表示空格边界 前后都算，即python的py也在边界上
result = re.findall(r'\w+\.py\b', msg)  # 要注意，\n \b本身在字符串内就有转义的作用，所以在正则中使用，字符串前面就要加r
print(result)  # 要注意.在正则中表示除了\n的任意字符
# \b匹配空格边界，即单词和空格间的位置
# \s匹配任意空白字符，等价于[\t\n\r\f]
# 对应的大写都表示非，如\S表示匹配任意'非'空白字符

# 分组 |的用法
# 匹配数字0-100
n = '69'
result = re.match('0$|[1-9]\d?$|100$', n)  # 注意这里的|的用法，表示'或'
print(result)

# 验证输入的邮箱  ()的用法
# (163|126|qq)代表整体的163或者126或者qq   [163|126|qq]则代表单个字符为'1','6','3','1','2','6','q','q'
# 验证输入的邮箱163，126，qq
mail = '23532@qq.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.com$', mail)
print(result)

# 不以4，7结尾的手机号码（11位）
num = '15332321608'
result = re.match(r'1\d{9}[0-35689]', num)
print(result)

# 分组的概念
# 提取电话号码 ()用来分组
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8}$)', phone)  # 以()为group的分组，一个()代表一组
print(result)
print(result.group())
print(result.group(1))  # 代表组1
print(result.group(2))  # 代表组2

# 引用分组的概念  引用分组有两种方式，一是number方式，二是(?P<名字>正则)方式
# 匹配标签
# number的应用  借助数字来达到分组前后的引用匹配  还可以借助起名的方式来实现分组匹配 \number
msg = '<html>abc</html>'
msg1 = '<html><h1>ABC</h1>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$', msg)
result1 = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg1)   # \1 代表对第一组()的原样引用，即必须和()内一致
print(result.group())
print(result.group(1))
print(result1)
#print(result1.group(2))

msg='<html><h1>ABC</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msg) # 利用数字实现原样引用
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))

# 借助起名的方式  在Django里有应用  注意?P要包含在()内  定义(?P<名字>正则)  使用(?P=名字)
result=re.match(r'<(?P<name1>[0-9a-zA-Z]+)><(?P<name2>[0-9a-zA-Z]+)>(.+)</(?P=name2)></(?P=name1)>$',msg)
print(result.group())
print(result.group(0))  # 注意，group(0)相当于group()，即全体
print(result.group(3))

# sub的应用  替换作用  sub(正则表达式,要替换为的新内容,待处理字符串)
result=re.sub(r'\d+','99','python:80,java:70')
print(result)

# sub中函数的应用
def func(temp):
    num=temp.group()
    num1=int(num)+1
    return str(num1)

result=re.sub(r'\d+',func,'python:80,java:70') # 拿一个匹配的就往函数里过一次，然后再拿一个匹配的再过一次
print(result)  # 这里只用传'函数对象'，不用加括号，否则表示调用了

# split 切片
result=re.split(r'[:,]','python:80,java:70')  # 遇到：或者,就分割，分割内容保存到列表中
print(result)  # ['python', '80', 'java', '70']

'''
系统预制的符号，如\w \d 等的定义在re模块里可以查询到
分组，涉及到()的使用，涉及到group()的使用。有匹配才能返回group，没匹配到就返回None。分组有number及name两种方式
'''

# python中的量词默认是贪婪的，尝试匹配尽可能多的字符
# 非贪婪则是尝试匹配尽可能少的字符
# 在量词"*","?","+","{m,n}"后面加上?,使贪婪变成非贪婪

msg='abc123abc'
result=re.match('abc\d+',msg) # <match='abc123'> 贪婪模式
print(result)
result=re.match('abc\d+?',msg) # <match='abc1'> 非贪婪模式
print(result)
