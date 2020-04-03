# 生成器，一个长列表，需要用到前面几个元素，列表元素可以按照某种算法推算出来，那么python一边循环一边不断计算出后续的元素
# 而不是一次性把所有的元素都计算出来，这种一边循环一边计算的机制，称为生成器generator
# iteration  迭代

list1 = [x for x in range(10)]
print(list1)
print(type(list1))

gene1 = (x for x in range(10))  # 用()定义生成器
print(gene1)
print(type(gene1))

print(gene1.__next__())  # 调用方式1
print(next(gene1))  # 调用方式2

while True:   # 如果元素被生成完了，继续生成就会报出StopIteration错误，故要用try
    try:
        print(next(gene1))
    except:
        print('元素已经取完~')
        break


# 生成器之函数
# 用函数定义生成器

def febo(m):
    n=0
    a,b=0,1
    while n<m:
        a,b=b,a+b
        n+=1                # 函数带yield，则就不再是函数了，变成了生成器
        yield b             # yield的作用相当于return加上暂停
    return '我是函数定义生成器的自定义异常信息，没有更多元素了~'

g=febo(10)
print('g的类型是',type(g))   # 可以看到febo(10)并没有实际执行函数，而只是生成了一个生成器
#print(type(next(g)))
print(next(g))              # 这里才是调用生成器的实际语句，以下为多次调用
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))              # 生成完所有元素后，生成器定义的return语句后的部分作为异常抛出
#print(next(g))


# 生成器的send方法
print('生成器的send方法演示******************')

def gen():
    n=0
    while n<5:
        #n += 1      # 这一行与第61行比较，能够看出yield的发生时刻
        temp = yield n
        n+=1
        print('temp的值是：',temp)
        print('n的值是：',n)
    return '没有更多数据了'

g=gen()
# g.send('第一次给temp传值')    # 注意这句，如果放在第一次执行生成器之前会报错，
# 错误为：TypeError: can't send non-None value to a just-started generator
#print(g.send(None))          # 这一句也和下面那个注释一样，直接会执行一次生成
print(g.__next__())
print('*********************')
g.send('第一次给temp传值')    # send起到了双重作用，一是给temp传值，二是直接执行了下一次的生成
print('*********************')
print(g.__next__())
print('*********************')
g.__next__()
print('*********************')
g.__next__()               # 因为有了g.send，所以到本行已经取完所有的n值了 n=4
# print(g.__next__())   # 没有g.send的话，那么到本行n取值已经取完，n=4

# -->既然可以通过g.send来给temp传值，那么传进去的temp值自然就可以参与生成器内部的运算<--


# 生成器   协程    迅雷下载的多线程，一个大文件分成一万份，10个线程每个线程负责1000份
# 进程>线程>协程   简单来说协程就是线程的小线程，可以交互执行
print()
print('以下是生成器用作协程的部分**************')

def task1(i):
    for x in range(i):
        print('搬了第{}块砖'.format(x))

def task2(i):
    for x in range(i):
        print('听了第{}首歌'.format(x))

task1(5)
task2(5)
print('这样只能实现顺序执行，搬完砖才能听歌')

print()
print('利用生成器进行协程，边搬砖边听歌')
def task1(i):
    for x in range(i):
        print('搬了第{}块砖'.format(x))
        yield

def task2(i):
    for x in range(i):
        print('听了第{}首歌'.format(x))
        yield


g1=task1(5)
g2=task2(5)
try:
    while True:
        g1.__next__()
        g2.__next__()
# except Exception as err:   注意这里有异常但没有被Exception所捕获，执行这里会得不到任何结果
#     print(err)
except:
    print('所有值已经取完了')



