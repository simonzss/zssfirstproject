# 模块
# 模块是代码组织的一种方式，把功能相近的类或者函数放到一个文件中，一个.py文件就是一个模块module，模块名就是文件名去掉.py

# 可以使用模块中定义的类、函数、变量

import module_calculate  # 首先会把模块内定义的所有东西加载到内存里，包括test()

print(module_calculate.list1)
print(module_calculate.add(*module_calculate.list1))
print(module_calculate.add(1, 2))
module_calculate.Calculate.show1()
m = module_calculate.Calculate(888)
m.show()

# 导入模块的三种方式
# 1、import 模块名      调用时要使用模块名.
# 2、from 模块名 import 类名|方法名|变量名    调用时就可以直接使用类名|方法名|变量名，不用前面加模块名,多个用,连接
# 3、from 模块名 import *      调用模块内所有的成员
# 如果想要限制*号获取的内容，可以在模块中使用__all__来指定*号可用的

# from module_calculate import add,number
from module_calculate import *  # import * 首先会把模块内定义的所有东西加载到内存里，包括test()

print(add(100, 100) + number)  # 这就是为什么test()会在所有行之前被执行
print(module_calculate.__name__) # __name__如果在引用它的其他类中，值等于定义它的本类的类名
# 如果希望调用时不自动执行test()方法，可以使用if __name__=='__main__':
# __name__如果在定义它的本类中，值等于__main__
# __name__如果在引用它的其他类中，值等于定义它的本类的类名，本例中为module_calculate
