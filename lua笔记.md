# Lua笔记

## 一、Lua特性

- 大小写敏感

- Lua只有对象类型，没有变量类型，所以定义变量就不需要声明类型

- Lua里的函数可以直接返回多个值

- 分号;用来标识一行结束

- Lua里面的小括号，仅用于函数，其他地方都不需要用

- a and b -- 如果a为false，则返回a，否则返回b

- a or b -- 如果a为true，则返回a，否则返回b

  ```lua
  function ccc(mytable)
      
  --mytable如果为不为空，则将mytable赋值给自己，如果为空则将空table赋值给mytable
  mytable=mytable or {};
  --仅当mytable的字段是string类型时才能用mytable.Name,别的就要用正式写法,比如mytable[1]
  mytable.Name="table";
  
  end
  ```

  

- 不加 **local** 的变量，全部都是全局变量，包括写在函数内部的都是全局变量，能直接被函数外面的代码访问

  - 一个文件里第一行上来就写 local a ，变量a实际也是全局变量，即：定义在全局里的局部变量，这个局部变量实际能被全局任何一个地方访问

- 数字只有一个 **number** 类型

- 连接符 ..

  - 字符串连接，如果操作数为数字，Lua将数字转成字符串

  - 连接符两边必须要有空格，连接符两边不管有多少个空格，都将被忽略 

    ```lua
    print("Hello" .. "World") --> HelloWorld
    
    print("Hello"       ..       "World") --> HelloWorld
    ```

- if用法示例，找出a,b,c中的最大值

  ```lua
  a=5
  b=3
  c=9
  
  Max=a
  
  if b>Max then
  Max=b
  end
  
  if c>Max then
  Max=c
  end
  
  print("最大值是" .. Max)
  ```

- while用法

  ```lua
  while (判断条件) do
  
  ...
  
  end
  ```

- for循环

  - 数值for循环

    ```lua
    --exp3可以省略，默认为1
    --exp1，exp2，exp3只会被计算一次，并且是在循环开始前
    --exp2如果是一个函数f(x),f(x)只会在循环前被调用一次
    --控制变量var是局部变量自动被声明，且只在循环内有效，不要试图去改var的值，容易逻辑错误
    for var=exp1，exp2，exp3 do
    
    loop-part
    
        --break,如果需要跳出循环，用break
        
    end
    ```

  - 范型for循环

    ```lua
    --对table里的数组key遍历
    for index,value in ipairs(table) do  --ipairs返回的是两个值，ipairs能保证遍历顺序
    
    print(value)
    
    end  --打印table里数组部分的所有值，非数组部分不管
    ```

    ```lua
    --对table进行字典遍历
    for key,value in pairs(table) do   --pairs返回的是两个值，pairs不能保证遍历顺序
    
    print(key,value)
    
    end
    ```

    ```lua
    --当仅有一个变量参与遍历时，意思是只遍历key，不遍历value
    
    for key in pairs(table) do  --pairs返回的是两个值，但只用变量key接收了第一个
    
    print(key)
    
    end
    ```

    

- return  函数返回值，每一个函数都有返回值，默认为nil

  - return后面必须跟end，遇到return函数结束，下面例子用提前的return使函数后面的语句不可能被执行

    ```lua
    function F()
    	do
    		print("aaa")
    		return "aaaa";
    	end
    print("bbb")
    return nil
    end
    
    F()
    print(F()) --这一句会输出aaa和aaaa
    
    ```



## 二、table

- 是Lua中唯一一个数据结构，自定义数据类型，通过table可以扩展出其他数据结构，比如数组、类

- Lua通过table来解决模块（module），包（package），对象（Object），和全局作用域（_G）

- table是 **引用类型** 的对象

- 除了nil，任何类型都可以作为table的key，包括函数

- 通过整数下标访问table中的元素即可简单地实现数组

- table的字段默认下标是从1开始的，不是从0开始

  ```lua
  --初始化表（创建空表）
  mytable={}
  
  
  --指定值
  mytable[1]="Lua"
  
  
  --移除引用
  mytable=nil  --lua垃圾回收会释放内存
  ```

  - table的方法：insert 

    ```lua
    --table.insert(table,[pos,]value)
    --注意，"apple"的字段名是1，"banana"的字段名是2，"orange"的字段名是3
    fruits={[-1]="-1",[0]="zero","apple","banana","orange"}
    table.insert(fruits,2,"grapes")
    print("索引为2的元素是 ",fruits[2]) -->"grapes"
    print("索引为3的元素是 ",fruits[3]) -->"banana"
    ```

    

  - table的方法：remove

    ```
    --table.remove(table[,pos])
    --删除并返回指定位置值，返回table数组部分位于pos位置的元素，其后的元素会被前移
    --pos参数可选，默认为table长度，即从最后一个元素删起
    fruits={[-1]="-1",[0]="zero","apple","banana","orange"}
    table.remove(fruits)  -->返回fruits最后一个元素，并从fruits中删除最后一个元素
    ```

    

  - table的方法：sort

    ```lua
    --table.sort(table[,comp]),[comp]比较函数，函数委托
    --对给定的table进行升序排序
    --pos参数可选，默认为table长度，即从最后一个元素删起
    fruits={[-1]="-1","apple","banana",[0]="zero","orange","grapes"}
    print("排序前")
    for k,v in ipairs(fruits) do
    print(k,v)
    end
    
    --table.sort(fruits) --升序
    table.sort(fruits,function(a,b)
    return a>b
    end) --降序
    -- a,b可以是两个table，return可以将两个table的字段拿来作为排序依据，比如a.id>b.id
    
    print("排序后")
    for k,v in ipairs(fruits) do
    print(k,v)
    end
    ```

  - table的嵌套，以及 **递归** 方式访问

    ```lua
    stu={}
    class={class=1,grade=1}   --第二行
    stu.classinfo=class;
    people={}
    people.kind=stu;
    people={["kind"]={["classinfo"]={["class"]=1,["grade"]=1},["key"]="key"}}
    --上面是一个三重嵌套的表，people表下嵌套stu表，stu表下嵌套class表，class表是第二行
    function tableToString(S)
        for v,k in pairs(S) do
            if type(k)=="table" then
                tableToString(k)  --强悍的递归，能够打印出所有的非表的值
            else
                print(v,k)
            end
        end
    end
    
    tableToString(people)
    
    --输出的结果是
    --grade	1
    --class	1
    --key	key
    ```

    ```lua
    --输出更美观的格式，自动添加花括号和缩进
    stu={}
    class={class=1,grade=1}   --第二行
    stu.classinfo=class;
    people={}
    people.kind=stu;
    people={["kind"]={["classinfo"]={["class"]=1,["grade"]=1},["key"]="key"},["weight"]=180}
    --上面是一个三重嵌套的表，people表下嵌套stu表，stu表下嵌套class表，class表是第二行
    function tableToString(S,tab)
    	tab=tab or "";  --上层的tab将带入下层
    
        for k,v in pairs(S) do
            if type(v)=="table" then
            	print(tab .. k .. ":")          --把key先打印出来
            	print(tab .. "{")               --打印出下层表的花括号
                tableToString(v,tab .. "    ")  --每次递归都在tab后加四个空格
                print(tab .. "}")               --打印出下层表的花括号
            else
                --print(k,v)
                print(tab .. k .. ":" .. v)
            end
        end
    end
    
    tableToString(people)
    --_G.tableToString(people)  --这句与上一句作用完全一样，
    
    --输出的结果相当漂亮，同层的元素都同列
    ```

  - Lua通过table来实现全局作用域:   _G表

    ```
    --上面的tableToString(S,tab)函数，可以写为table.ToString(S,tab)
    stu={}
    class={class=121,grade=1}
    function table.ToString(S,tab)
    
    _G.table.ToString(S) --是在_G下的table字段下value里添加了ToString字段
    _G={table={ToString=ToString函数的内存地址}}
    
    而tableToString(S)，是在_G下添加了字段tableToString
    _G={table={...},tableToString=tableToString函数的内存地址,stu={},class={class=121,grade=1}}
    因此可以print(_G.class.class)，结果为121
    ```

  - Lua里的table可以被重写

    ```
    --定义了table为名称的函数，在_G里的table字段对应的值就只是一个函数，不是表了
    function table()  
    print("table变成了函数类型")
    end
    --不要这么干！如果需要重写_G下的table，用下面的办法
    
    __table=table
    --修改table，甚至可以table=1
    table=__table  --再把原生table还回去
    ```

    



















