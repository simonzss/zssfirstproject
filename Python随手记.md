# 命令行窗口中python -c 的用法

python -c "import sys;print(sys.path)"

# sys.path

一个由字符串组成的列表，用于指定模块的搜索路径。初始化自环境变量 PYTHONPATH，再加上一条与安装有关的默认路径。

程序启动时将初始化该列表，列表的第一项 path[0] 目录含有调用 Python 解释器的脚本。如果脚本目录不可用（比如以交互方式调用了解释器，或脚本是从标准输入中读取的），则 path[0] 为空字符串，这将导致 Python 优先搜索当前目录中的模块。注意，脚本目录将插入在 PYTHONPATH 的条目*之前*。

程序可以随意修改本列表用于自己的目的。只能向 sys.path 中添加 string 和 bytes 类型，其他数据类型将在导入期间被忽略。

参见 site 模块，该模块描述了如何使用 .pth 文件来扩展 sys.path。



# PYTHONPATH

增加模块文件默认搜索路径。 所用格式与终端的 PATH 相同：一个或多个由 os.pathsep 分隔的目录路径名称（例如 Unix 上用冒号而在 Windows 上用分号）。 默认忽略不存在的目录。

除了普通目录之外，单个 PYTHONPATH 条目可以引用包含纯Python模块的zip文件（源代码或编译形式）。无法从zip文件导入扩展模块。

默认索引路径依赖于安装路径，但通常都是以 prefix/lib/pythonversion 开始 (参见上文中的 PYTHONHOME)。 它 总是 会被添加到 PYTHONPATH。

有一个附加目录将被插入到索引路径的 PYTHONPATH 之前，正如上文中 接口选项 所描述的。 搜索路径可以在 Python 程序内作为变量 sys.path 来进行操作。

# sys.argv

一个列表，其中包含了被传递给 Python 脚本的命令行参数。 argv[0] 为脚本的名称（是否是完整的路径名取决于操作系统）。如果是通过 Python 解释器的命令行参数 -c 来执行的， argv[0] 会被设置成字符串 '-c' 。如果没有脚本名被传递给 Python 解释器， argv[0] 为空字符串。



# 2.1.1. 传入参数

如果可能的话，解释器会读取命令行参数，转化为字符串列表存入 sys 模块中的 argv 变量中。执行命令 import sys 你可以导入这个模块并访问这个列表。这个列表最少也会有一个元素；如果没有给定输入参数，sys.argv[0] 就是个空字符串。如果脚本名是 '-'``（标准输入）时，``sys.argv[0] 就是 '-'。使用 -c 命令 时，sys.argv[0] 就会是 '-c'。如果使用选项 -m module，sys.argv[0] 就是包含目录的模块全名。在 -c command 或 -m module 之后的选项不会被解释器处理，而会直接留在 sys.argv 中给命令或模块来处理。

#例如  python -c "import sys;print(sys.path);print(sys.argv)" flask db init    sys.argv的结果是['-c', 'flask', 'db', 'init']



# 切片的包头不包尾

注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s

注意以下，既包又不包，结果就是不包

```
>>>list(range(10,10))
[]
```




# 可迭代对象
range() 所返回的对象在许多方面表现得像一个列表，**但实际上却并不是**。此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，这样就能节省空间。

```
>>>print(range(10))
range(0, 10)
>>>list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

我们称这样对象为 iterable，也就是说，适合作为这样的目标对象：函数和结构期望从中获取连续的项直到所提供的项全部耗尽。 我们已经看到 for 语句就是这样一种结构，而接受可迭代对象的函数的一个例子是 sum():

```
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```



## `break` 、 `continue` 以及循环中的 `else` 子句

[`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句，和 C 中的类似，用于跳出最近的 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 或 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 循环.

循环语句可能带有 `else` 子句；它会在循环耗尽了可迭代对象 (使用 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for)) 或循环条件变为假值 (使用 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while)) 时被执行，但不会在循环被 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句终止时被执行。

[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 语句也是借鉴自 C 语言，表示继续循环中的下一次迭代



# 函数

函数的 *执行*（*execution*） 会引入一个用于函数局部变量的新符号表。 更确切地说，函数中所有的变量赋值都将存储在局部符号表中；而变量引用（variable references）会首先在**局部符号表**（the local symbol table）中查找，然后是**外层函数的局部符号表**（the local symbol tables of enclosing functions），再然后是**全局符号表**（the global symbol table），最后是**内置名称的符号表**（the table of built-in names）。 因此，全局变量和外层函数的变量不能在函数内部直接赋值（除非是在 [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句中定义的全局变量，或者是在 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句中定义的外层函数的变量），尽管它们可以被引用。

在函数被调用时，实际参数们（实参arguments）会被引入被调用函数的**局部符号表**中；因此，实参是通过 **按值调用**（*call by value*）传递的（其中 值（value） 始终是**对象引用**（object reference）而不是对象的值）。[1](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#id2) 当一个函数调用另外一个函数时，将会为该调用创建一个新的局部符号表(a new local symbol table)。

函数定义会将函数名称与函数对象在当前符号表中进行关联。 解释器会将该名称所指向的对象识别为用户自定义函数。 其他名称也可指向同一个函数对象并可被用来访问访函数:





### [形参和实参之间有什么区别？](https://docs.python.org/zh-cn/3/faq/programming.html#id16)

[形参](https://docs.python.org/zh-cn/3/glossary.html#term-parameter) （**parameter**）是指出现在函数定义中的名称，而 [实参](https://docs.python.org/zh-cn/3/glossary.html#term-argument) （argument）则是在调用函数时实际传入的值。 形参定义了一个函数能接受何种类型的实参。 例如，对于以下函数定义:

```
def func(foo, bar=None, **kwargs):
    pass
```

*foo*, *bar* 和 *kwargs* 是 `func` 的形参。 但是，在调用 `func` 时，例如：

```
func(42, bar=314, extra=somevar)
```

实际的值 `42`, `314` 和 `somevar` 则是实参。



### 4.7.1. 默认实参值

最有用的形式是对一个或多个参数指定一个默认值。这样创建的函数，可以用比定义时允许的更少的参数调用，比如:

def ask_ok(prompt, **retries=4**):

**retries=4**为默认值参数



**重要警告：** 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:

```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

这将打印出

```
[1]
[1, 2]
[1, 2, 3]
```

如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:

```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```



### 4.7.2. 关键字实参

也可以使用形如 `kwarg=value` 的 [关键字实参](https://docs.python.org/zh-cn/3/glossary.html#term-keyword-argument) 来调用函数。例如下面的函数:

在函数调用中，关键字实参必须跟随在位置实参的后面。

当存在一个形式为 `**name` 的最后一个形参时，这个形参会接收一个字典 (参见 [映射类型 --- dict](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesmapping))，其中包含除了与已有形参相对应的关键字参数以外的所有关键字实参。 这可以与一个形式为 `*name`，接收一个包含除了已有形参列表以外的位置实参的 [元组](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-tuples) 的形参 (将在下一小节介绍) 组合使用 (`*name` 必须出现在 `**name` 之前。) 例如，如果我们这样定义一个函数:

### 4.7.3. 特殊形参

默认情况下，实参传递形式可以通过**位置**或者**显式的关键字**。 为了确保可读性和运行效率，限制实参传递的方式是有意义的，这样开发者只需查看函数定义即可确定参数项是仅按位置、按位置或按关键字，还是仅按关键字传递。

函数的定义看起来可以像是这样：

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

在这里 `/` 和 `*` 是可选的。 如果使用，这些符号通过实参如何传递给函数的方式表明了形参的种类：仅限位置、位置或关键字，以及仅限关键字。 关键字形参也被称为命名形参（named parameters）。



#### 4.7.3.4. 函数示例

请考虑以下示例函数定义并特别注意 `/` 和 `*` 标记:

```
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```

第一个函数定义 `standard_arg` 是最常见的形式，对调用方式没有任何限制，**实参可以按位置也可以按关键字传入**:

\>>>

```
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2
```

第二个函数 `pos_only_arg` 在函数定义中带有 `/`，限制仅使用位置形参。:

\>>>

```
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got an unexpected keyword argument 'arg'
```

第三个函数 `kwd_only_args` 在函数定义中通过 `*` 指明仅允许关键字实参:

\>>>

```
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3
```



### 4.7.4. 任意的参数列表

最后，最不常用的选项是可以使用任意数量的参数调用函数。这些参数会被包含在一个元组里（参见 [元组和序列](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-tuples) ）。在可变数量的参数之前，可能会出现零个或多个普通参数。:

一般来说，这些 `可变参数`（`*args`） 将在形式参数列表的末尾，因为它们收集传递给函数的所有剩余输入参数。出现在 `*args` 参数之后的任何形式参数都是 ‘仅限关键字参数’，也就是说它们只能作为关键字参数而不能是位置参数。:

个人理解：这里说的是调用函数时，如果可变参数还未明确定义（参数形参化），那么可以将任意多个实参给与**可变参数**，任意多个实参将被打包在一个元组里



### 4.7.5. 解包实参列表

当实参已经在列表或元组中但要为需要单独位置实参的函数调用解包时，会发生相反的情况。例如，内置的 [`range()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 函数需要单独的 *start* 和 *stop* 参数。如果它们不能单独使用，可以使用 `*` 操作符 来编写函数调用以便从列表或元组中解包参数:

同样的方式，字典可使用 `**` 操作符 来提供关键字参数。

\>>>

```
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```

个人理解：这里说的是调用函数时，如果可变参数已经在调用函数前明确定义（参数实参化），则可变参数按照调用函数的要求进行解包





### 4.7.6. Lambda 表达式

可以用 [`lambda`](https://docs.python.org/zh-cn/3/reference/expressions.html#lambda) 关键字来创建一个小的匿名函数。这个函数返回两个参数的和： `lambda a, b: a+b` 。Lambda函数可以在需要函数对象的任何地方使用。它们在语法上限于单个表达式。从语义上来说，它们只是正常函数定义的语法糖。与嵌套函数定义一样，lambda函数可以引用所包含域的变量（Like nested function definitions, lambda functions can reference variables from the containing scope）

另一个用法是传递一个小函数作为参数:

\>>>

```
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```



lambda    是匿名的函数，冒号前代表函数参数，冒号后代表函数返回值



### 4.7.8. 函数标注

[函数标注](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function) 是关于用户自定义函数中使用的类型的完全可选元数据信息（有关详情请参阅 [**PEP 3107**](https://www.python.org/dev/peps/pep-3107) 和 [**PEP 484**](https://www.python.org/dev/peps/pep-0484) ）。

[函数标注](https://docs.python.org/zh-cn/3/glossary.html#term-function-annotation) 以字典的形式存放在函数的 `__annotations__` 属性中，并且不会影响函数的任何其他部分。 形参标注的定义方式是在形参名称后加上冒号，后面跟一个表达式，该表达式会被求值为标注的值。 返回值标注的定义方式是加上一个组合符号 `->`，后面跟一个表达式，该标注位于形参列表和表示 [`def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def) 语句结束的冒号之间。 下面的示例有一个位置参数，一个关键字参数以及返回值带有相应标注:

\>>>

```
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

个人理解：标注就是函数内的注释，用来说明形参和返回值的类型，形参标注在形参后加:表达式，返回值标注在函数括号与冒号之间加->表达式



# 什么是表达式

一种高级语言的任何程序代码，如果（如果）执行终止，将返回一个值。在大多数编程语言中，表达式由常量，变量，运算符，函数和括号组成。运算符和功能可以是内置的或用户定义的。语言在如何组合不同类型的表达式方面有所不同-通过显式强制转换和隐式强制的某种组合。

尽管某些语言（例如Lisp或Forth）具有自己的特有语法，但是表达式的语法通常遵循常规的数学符号。



# 列表

你可能已经注意到，像 `insert` ，`remove` 或者 `sort` 方法，只修改列表，没有打印出返回值——它们返回默认值 `None` 。[1](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#id2) 这是Python中所有可变数据结构的设计原则。

列表可以用作队列，所谓队列就是“先进先出”，但列表队列很低效

若要实现一个队列，可使用 [`collections.deque`](https://docs.python.org/zh-cn/3/library/collections.html#collections.deque)，它有popleft()和popright()方法



列表推导式

列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，后面跟一个 `for` 子句，然后是零个或多个 `for` 或 `if` 子句。 **其结果将是一个新列表**，由对表达式依据后面的 `for` 和 `if` 子句的内容进行求值计算而得出。

列表推导式的结果是**列表**，这对理解列表推导式的嵌套很有帮助



# 初识序列(列表、字符串、元组)

我们看到列表和字符串有很多共同特性，例如索引和切片操作。他们是 *序列* 数据类型。元组也是序列数据类型。

虽然元组可能看起来与列表很像，但它们通常是在不同的场景被使用，并且有着不同的用途。元组是 [immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable) ，其序列通常包含不同种类的元素，并且通过解包（这一节下面会解释）或者索引来访问（如果是 [`namedtuples`](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple) 的话甚至还可以通过属性访问）。列表是 [mutable](https://docs.python.org/zh-cn/3/glossary.html#term-mutable) ，并且列表中的元素一般是同种类型的，并且通过迭代访问。

元组打包

```
>>>t=1,2,'hello'
>>>t
(1, 2, 'hello')
```

元组解包

```
>>>x,y,z=t
>>>t
(1, 2, 'hello')
>>>x
1
>>>y
2
>>>z
'hello'
```



# 集合

同数学概念，不重复且无序，花括号或 [`set()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 函数可以用来创建集合。注意：要创建一个空集合你只能用 `set()` 而不能用 `{}`，因为后者是创建一个空字典

类似于 [列表推导式](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-listcomps)，集合也支持推导式形式



# 字典

- 字典属于映射类型

- 与以连续整数为索引的序列不同，字典是以 **关键字** 为索引的，关键字可以是**任意不可变类型**，通常是字符串或数字。如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字。

- 理解字典的最好方式，就是将它看做是一个 *键: 值* 对的集合，**键必须是唯一的**（在一个字典中）。

- 字典主要的操作是使**用关键字存储和解析值**。

- 对一个字典执行 `list(d)` 将返回包含该字典中所有键的列表，按插入次序排列 (如需其他排序，则要使用 `sorted(d)`)。要检查字典中是否存在一个特定键，可使用 [`in`](https://docs.python.org/zh-cn/3/reference/expressions.html#in) 关键字

- 此外，字典推导式可以从任意的键值表达式中创建字典

  ```
  >>> {x: x**2 for x in (2, 4, 6)}
  {2: 4, 4: 16, 6: 36}
  ```
  - 个人理解：理解并查看某某推导式，最重要的是第一个for前面是什么表达式，注意x: x**2也是一个表达式，其次要看推导式外面包围的是方括号（列表推导式）还是花括号(集合推导式、字典推导式)

## 5.6. 循环的技巧

- 当在字典中循环时，用 `items()` 方法可将关键字和对应的值同时取出

- 当在序列中循环时，用 [`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate) 函数可以将索引位置和其对应的值同时取出
- 当同时在两个或更多序列中循环时，可以用 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 函数将其内元素一一匹配
- 如果要逆向循环一个序列，可以先正向定位序列，然后调用 [`reversed()`](https://docs.python.org/zh-cn/3/library/functions.html#reversed) 函数
- 如果要按某个指定顺序循环一个序列，可以用 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列
- 有时可能会想在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的



## 5.7. 深入条件控制

- 比较操作符 `in` 和 `not in` 校验一个值是否在（或不在）一个序列里。操作符 `is` 和 `is not` 比较两个对象是不是同一个对象，这只对像列表这样的可变对象比较重要。
- 布尔运算符 `and` 和 `or` 也被称为 *短路* 运算符：它们的参数从左至右解析，一旦可以确定结果解析就会停止。
- 请注意 Python 与 C 不同，在表达式内部赋值必须显式地使用 [海象运算符](https://docs.python.org/zh-cn/3/faq/design.html#why-can-t-i-use-an-assignment-in-an-expression) `:=` 来完成。个人理解：表达式内部赋值，就是在表达式内部给表达式起一个名字，以供别处引用

## 5.8. 比较序列和其他类型

- 序列对象通常可以与相同序列类型的其他对象比较。 这种比较使用 *字典式* 顺序：首先比较开头的两个对应元素，如果两者不相等则比较结果就由此确定；如果两者相等则比较之后的两个元素，以此类推，直到有一个序列被耗尽。 如果要比较的两个元素本身又是相同类型的序列，则会递归地执行字典式顺序比较。 如果两个序列中所有的对应元素都相等，则两个序列也将被视为相等。 如果一个序列是另一个的初始子序列，则较短的序列就被视为较小（较少）。 对于字符串来说，字典式顺序是使用 Unicode 码位序号对单个字符排序。 下面是一些相同类型序列之间比较的例子：

  ```
  (1, 2, 3)              < (1, 2, 4)
  [1, 2, 3]              < [1, 2, 4]
  'ABC' < 'C' < 'Pascal' < 'Python'
  (1, 2, 3, 4)           < (1, 2, 4)
  (1, 2)                 < (1, 2, -1)
  (1, 2, 3)             == (1.0, 2.0, 3.0)
  (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
  ```

- 递归：程序调用自身的编程技巧称为*递归*（ recursion）
-  如果要比较的两个元素本身又是相同类型的序列，则会递归地执行字典式顺序比较。 这里递归的意思是说，假设大序列对象内部的某个元素是小序列对象，实现大序列对象的比较功能的代码假设为一个函数，那么在比较内部的小序列对象时，同样是使用这个函数实现的。



# 6. 模块

- 用文本编辑器为解释器准备输入并将该文件作为**输入运行**。这被称作编写 *脚本* 。
- *主* 模块（你在顶级和计算器模式下执行的脚本中可以访问的变量集合）。
- 模块是一个包含Python定义和语句的文件。文件名就是模块名后跟文件后缀 `.py` 。在一个模块内部，模块名（作为一个字符串）可以通过全局变量 `__name__` 的值获得。

# 6.1 更多有关模块的信息

- 模块可以包含可执行的语句以及函数定义。这些语句用于初始化模块。它们仅在模块 *第一次* 在 import 语句中被导入时才执行。 [1](https://docs.python.org/zh-cn/3/tutorial/modules.html#id2) (当文件被当作脚本运行时，它们也会执行。)

- 每个模块都有它自己的私有符号表，该表用作模块中定义的所有函数的**全局符号表**。

- 被导入的模块名存放在调入模块的全局符号表中。（The imported module names are placed in the importing module’s global symbol table.）

- [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句有一个变体，它可以把名字从一个被调模块内直接导入到**现模块**的符号表里。例如:

  \>>>

  ```
  >>> from fibo import fib, fib2
  >>> fib(500)
  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
  ```

  这并不会把**被调模块名**引入到局部变量表里（因此在这个例子里，`fibo` 是未被定义的）。

  This does not introduce the module name from which the imports are taken in the local symbol table。   be taken 被采取，被采用

- 还有一个变体甚至可以导入模块内定义的所有名称:

  \>>>

  ```
  >>> from fibo import *
  >>> fib(500)
  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
  ```

  这会调入所有**非以下划线**（`_`）开头的名称。 在多数情况下，Python程序员都不会使用这个功能

- 如果模块名称之后带有 `as`，则跟在 `as` 之后的名称将直接绑定到所导入的模块。意思就是将原有模块名称as为别名

- 6.1.1. 以脚本的方式执行模块，模块的 `__name__` 会被赋值为 `"__main__"`。

- ### 6.1.2. 模块搜索路径

  - 先找内置模块，看有没有
  - 再从[`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 变量给出的目录列表里寻找，[`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 初始有这些目录地址:
    - 包含输入脚本的目录（或者未指定文件时的当前目录）。
    - [`PYTHONPATH`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) （一个包含目录名称的列表，它和shell变量 `PATH` 有一样的语法）。
    - 取决于安装的默认设置
  - **在初始化后**，Python程序可以更改 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path)。**包含正在运行脚本的文件目录**被放在搜索路径的**开头**处， **在标准库路径之前**。

- ## 6.3. [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 函数

  - 内置函数 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 用于查找**模块定义的名称**。 它返回一个**字符串列表**，这个列表是排序过的
  - 如果没有参数，[`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 会列出你当前定义的名称。它列出所有类型的名称：变量，模块，函数，等等
  - [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 不会列出内置函数和变量的名称。如果你想要这些，它们的定义是在标准模块 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 中

# 6.4. 包

- 当使用 `from package import item` 时，item可以是包的子模块（或子包），也可以是包中定义的其他名称，如函数，类或变量。

-  `import` 语句首先测试是否在包中定义了item；如果没有，它假定它是一个模块并尝试加载它。如果找不到它，则引发 [`ImportError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError) 异常。

- 相反，当使用 `import item.subitem.subsubitem` 这样的语法时，除了最后一项之外的每一项都必须是一个包；最后一项可以是模块或包，但不能是前一项中定义的类或函数或变量。

  ## 6.4.2. 子包参考

- 请注意，相对导入是基于当前模块的名称进行导入的。由于主模块的名称总是 `"__main__"` ，因此用作Python应用程序主模块的模块必须始终使用绝对导入。

  

# 7.输入输出

# 8. 错误和异常

# 9. 类

## 9.1. 名称和对象

- 对象具有个性，多个名称（在多个作用域内）可以绑定到同一个对象。这在其他语言中称为别名。

## 9.2. Python 作用域和命名空间

- *namespace* （命名空间）是一个从**名字**到**对象**的映射。 大部分命名空间当前都由 Python 字典实现

- 任何跟在一个点号之后的名称都称为 *属性*（*attribute* ）

- 在不同时刻创建的命名空间拥有不同的生存期。包含内置名称(the built-in names)的命名空间是在 Python 解释器启动时创建的，永远不会被删除。模块的全局命名空间在模块定义被读入时创建；通常，模块命名空间也会持续到解释器退出。被解释器的顶层调用执行的语句，无论是从一个脚本文件读取的还是交互式地读取的，都被认为是 [`__main__`](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 模块调用的一部分，因此它们拥有自己的全局命名空间。（内置名称实际上也存在于一个模块中；这个模块称作 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 。）

- 一个函数的本地命名空间在这个函数被调用时创建，并在函数返回或抛出一个不在函数内部处理的错误时被删除。（事实上，比起描述到底发生了什么，忘掉它更好。）当然，每次递归调用（recursive invocations）都会有它自己的本地命名空间。

- 一个 *作用域* 是一个可直接访问命名空间的 Python 程序的文本区域。 这里的 “可直接访问” 意味着对名称的非限定引用（an unqualified reference）会尝试在命名空间中查找名称。

  A *scope* is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

- Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes(嵌套的作用域) whose namespaces are directly accessible:

  - the innermost scope, which is searched first, contains the local(局部) names
  - the scopes of any enclosing(封闭) functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
  - the next-to-last scope contains the current module’s global(全局) names
  - the outermost scope (searched last) is the namespace containing built-in(内置) names

- If a name is declared global, then all references(引用) and assignments(赋值) go directly to the middle scope containing the module’s global names. To rebind variables found outside of the innermost scope, the [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement can be used; if not declared nonlocal, those variables are read-only (an attempt to write to such a variable will simply create a *new* local variable in the innermost scope, leaving the identically named outer variable unchanged).

- Usually, the local scope references the local names of the (textually) current function. Outside functions, the local scope references the same namespace as the global scope: the module’s namespace. Class definitions place yet another namespace in the local scope.

  It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module’s namespace, no matter from where or by what alias the function is called. On the other hand, the actual search for names is done dynamically, at run time — however, the language definition is evolving towards static name resolution, at “compile” time, so don’t rely on dynamic name resolution! (In fact, local variables are already determined statically.)

- Python 的一个特殊规定是这样的 -- 如果不存在生效的 [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 或 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句 -- 则对名称的赋值总是会进入最内层作用域。 赋值不会复制数据 --- 它们只是将名称绑定到对象。 删除也是如此：语句 `del x` 会从局部作用域所引用的命名空间中移除对 `x` 的绑定。 事实上，所有引入新名称的操作都是使用局部作用域：值得一提的是，[`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句和函数定义会在局部作用域中绑定模块或函数名称。

  [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；[`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句表明特定变量生存于封闭作用域中并且应当在其中被重新绑定。

## 9.3. 初探类



