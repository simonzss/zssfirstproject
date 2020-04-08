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
# 如果想要限制*号获取的内容，可以在模块中使用__all__来指定*号可用的，注意__all__的作用只是用来指定*号的范围

# from module_calculate import add,number
from module_calculate import *  # import * 首先会把模块内定义的所有东西加载到内存里，包括test()

print(add(100, 100) + number)  # 这就是为什么test()会在所有行之前被执行
print(module_calculate.__name__) # __name__如果在引用它的其他类中，值等于定义它的本类的类名
# 如果希望调用时不自动执行test()方法，可以使用if __name__=='__main__':
# __name__如果在定义它的本类中，值等于__main__
# __name__如果在引用定义它的本类的其他类中，值等于定义它的本类的类名，本例中为module_calculate


# 包含相对路径import 的python脚本不能'直接运行'，只能作为module被引用
# Note that relative imports are based on the name of the current module.
# Since the name of the main module is always"__main__",
# modules intended for use as the main module of a Python application must always use absolute imports.

# from的起点是项目，因此内层调外层，直接写外层.就可以
# 包内__init__.py文件的用途是，当导入包时，默认一定先导入__init__.py文件，内存有包了，就会同时执行__init__.py
# 因此一般把一些初始化的函数|变量|类定义在__init__.py文件中
# __init__.py文件中的成员的访问，直接通过包名.成员名，而不是包名.__init__.成员名
# from 包名 import * 时，包中的__init__.py必须定义__all__,谁在__all__里谁才能被默认加载，这与from 模块 import * 不同
# from 包名 import * 时，默认是不加载'包'中的任何一个模块
# from 模块 import * 时，默认是加载'模块'中的所有成员


# 模块的循环导入
# 1、这是一个架构错误，要尽量避免循环导入的出现
# 2、解决方法有二，一是将'from 模块 import 成员'写入当前模块的函数中，二是将'from 模块 import 成员'写在当前模块的最后
# 在解决循环导入的过程中，经常用if __name__=='__main__'来让被加载的模块'只加载不执行'
# 推荐将'from 模块 import 成员'写入当前模块的函数中解决模块的循环导入问题