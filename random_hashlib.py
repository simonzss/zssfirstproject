# random模块

import random

ran=random.random()  # 生成0-1之间的随机小数
print(ran)

ran=random.randrange(1,10,2) # 生成1-10之间的随机数，2为步长，从1，3，5，7，9中随机取
print(ran)

ran=random.randint(1,5)    # 包右
print(ran)

list1=['zhangsan','lisi','wangwu','zhaoliu']
ran=random.choice(list1)
print(ran)


# shuffle 洗牌
list2=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(list2) # Shuffle list x in place, and return None
print(list2)

# 验证码，大小写字母与数字的组合
def enter_code():
    s=''
    for i in range(4):
        ran1=str(random.randint(0,9))
        ran2=chr(random.randint(65,90))
        ran3=chr(random.randint(97,122))
        list_ran = [ran1, ran2, ran3]
        ran=random.choice(list_ran)
        s+=ran
    return s

print(enter_code())

# chr 和 ord
print(chr(65))  # 从Unicode码转为字符串
print(ord('A')) # 从字符串转为Unicode码
print(ord('姝'))

# 加密算法 hashlib
# 加密算法：md5 sha1 sha256等都是单向不可逆的，只能加密，无法解密
# 而base64这种加密算法是可逆的
import hashlib

msg='等又再等为你等又再等始终等你不到'
md5=hashlib.md5(msg.encode('utf-8'))
# hashlib.md5不能直接加密中文，所以要先把中文转换为utf-8编码，然后对utf-8编码进行加密

print(md5)              # <md5 HASH object @ 0x000001D2A55802F0>
print(md5.hexdigest())  # 打印加密结果

# 第三方模块    pillow 图像文件处理    requests 浏览器操作