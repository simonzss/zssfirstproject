# 异常处理
"""
try:
    可能出现异常的代码
except 异常类型1:                                    自上而下逐一匹配异常类型，匹配到就不再继续匹配
    如果发生了异常执行的代码
except 异常类型2:
    如果发生了异常执行的代码
...可以有多个except
except Exception as err:   注意这个Exception必须放最下面
    print(err)
[finally:
    无论是否出现异常都会被执行的代码]

"""

#int('a')
def exam():
    try:
        list1=[1]
        list1.pop()
        int('1')
        return '1'    #如果使用了else，那么try代码中就不能出现return
    except ValueError:
        print('精准定位到ValueError错误')
    except Exception as err:
        print('出错了',err)
    else:  #try不出'任何'错误才会执行      如果使用了else，那么try代码中就不能出现return
        print('一切顺利')
    finally:
        print('finally使用的场景例子：stream.close(),无论前面是否有错，最后都应该关闭流')
        return "finally级别最优先,注意这里没有return出try代码块中的'1'"

x=exam()
print(x)