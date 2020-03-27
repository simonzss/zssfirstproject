import random
# 函数运行四部曲
# 1.import   函数运行第一步

# 2.定义函数  函数运行第二步   定义就代表给函数分配了内存地址  定义的东西都要往内存加载
def generate_random():
    for num in range(10):
        ran = random.randint(1, 20)
        print(ran)

# 3.这里就可以访问函数内存地址  函数运行第三步
print(generate_random)   #打印函数名就是打印函数的内存地址

# 4.调用函数  函数名加括号  函数的调用，实际就是去访问定义函数时给的内存地址   函数运行第四步
generate_random()  # generate_random代表函数地址  而()代表调用  图形理解就是  函数名定下内存地址，()符号决定调用此内存地址下的函数体
print('------------------')
generate_random()