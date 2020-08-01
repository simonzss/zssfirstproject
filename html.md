# HTML

* html是一种标记语言，标记语言是一套标记标签，用标记标签来描述网页
* html文档是由html标签定义的，标签不区分大小写，建议全部小写



# HTML元素

* html元素指的是从开始标签到结束标签的所有代码，注意是包含开始标签和结束标签的

  * ```
    <p>This is my first paragraph.</p>
    这个 <p> 元素定义了 HTML 文档中的一个段落。
    这个元素拥有一个开始标签 <p>，以及一个结束标签 </p>。
    元素内容是：This is my first paragraph。
    ```

* 大多数html元素拥有属性，属性只声明于开始标签



# HTML DOM(Document Object Model)

- **HTML DOM 是关于如何获取、更改、添加或删除 HTML 元素的标准**
- HTML DOM 定义了：
  - 作为**对象**的 HTML 元素
  - 所有 HTML 元素的*属性*
  - 访问所有 HTML 元素的*方法*
  - 所有 HTML 元素的*事件*
- 整个文档是一个文档节点树
- html元素指的是从开始标签到结束标签的所有代码，元素节点
- html元素内的Text文本是文本节点
- 元素如果拥有属性，属性还会被解析为属性节点
- 注释是注释节点



# web服务器

- 大多数web服务器对大小写敏感，london.jpg不能通过London.jps访问
- IIS对大小写不敏感
- html文件的扩展名，htm和html没有区别，htm是因为早期dos系统扩展名只能有三个字符



# HTML语法

- html是大小写不敏感的，通常使用全小写
- =前后可以使用空格，但不推荐
- 注释为<!-- 注释内容 -->



# HTML元素的属性

- 属性总是在 HTML 元素的*开始标签*中规定。

  属性总是以名称/值对的形式出现，比如：*name="value"*。

  所有属性都有默认值

- id属性是唯一的

- class属性可以为元素定义一个或者多个类名

- style规定元素的行内样式

- title描述元素的额外信息



# HTML常用标签

- 百度搜索**HTML标签简写及全称大全**

- \<h1>标题    \<p>段落	\<a>链接	\<img>图像	\<table>表格

- \<table>表格有\<tr>,table row

- \<table>表格有\<td>,table data

- \<table>表格有\<th>,table header

- \<table>表格有\<caption>,表格标题

- \<ul>unordered lists

- \<ol>ordered lists

- \<li>list item

- \<form>表单

  - 输入元素都必须带name属性，服务器将name属性作为传递数据值的标识
  - 如果需要设置默认值，则用value属性
  - 提交方式有GET和POST，GET提交以浏览器地址栏明文URL提交
  - POST通过request body加密传递参数

- “块级元素”译为 block level element，“内联元素”译为 inline element

- 元素的display属性确定了元素类型，"block"块级元素，"inline"内联元素

- \<div>Division分隔

  - \<div> 元素是块级元素，它是可用于组合其他 HTML 元素的容器

  - 块级元素在浏览器显示时，通常会以新行来开始（和结束）。

    例子：<h1>, <p>, <ul>, <table>

- \<span>Span范围

  -  \<span> 元素是内联元素，可用作文本的容器。可以用作内联元素的容器。

  - 内联元素在显示时通常不会以新行开始。

    例子：<b>, <td>, <a>, <img>

- \<hr>Horizontal Rule水平尺

- \<br>Break换行

- \<frameset>框架，可以在同一个浏览器窗口中显示不止一个页面



# CSS(Cascading Style Sheets)

- CSS是一种标记语言，可以直接由浏览器执行

- 层叠的概念，作用于同一个HTML元素时，不同的样式层叠合并为一，相同的样式按优先级覆盖

- 优先级

  - 外部样式表（独立于HTML的CSS文档）
  - 内部样式表（位于 \<head> 标签内部）
  - 内联样式（在 HTML 元素内部）

- 语法规则

  - ```
    selector {property: value; property: value; ... property: value;}
    ```

  - 选择器{属性:值}，例如

  - ```
    h1 {color:red; font-size:14px;}
    ```

- 外部样式表

  - 当样式需要应用于很多页面时，外部样式表将是理想的选择

  - 使用\<link> 标签链接到样式表。\<link> 标签在（文档的）头部。\<link>标签属于HTML

  - ```
    <head>
    <link rel="stylesheet" type="text/css" href="mystyle.css" />
    </head>
    ```

  - 外部样式表可以在任何文本编辑器中进行编辑。文件不能包含任何的 html 标签。样式表应该以 .css 扩展名进行保存。

- 内部样式表

  - 当单个文档需要特殊的样式时，就应该使用内部样式表

  - 使用\<style> 标签在文档头部定义内部样式表

  - ```
    <head>
    <style type="text/css">
      hr {color: sienna;}
      p {margin-left: 20px;}
      body {background-image: url("images/back40.gif");}
    </style>
    </head>
    ```

- 内联样式

  - 由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。请慎用这种方法，例如当样式仅需要在一个元素上应用一次时

  - 在相关的标签内使用样式（style）属性。Style 属性可以包含任何 CSS 属性。本例展示如何改变段落的颜色和左外边距：

    ```
    <p style="color: sienna; margin-left: 20px">
    This is a paragraph
    </p>
    ```



# CSS选择器

- 元素选择器

  - 最常见的 CSS 选择器是元素选择器。换句话说，文档的元素就是最基本的选择器

- 选择器分组和声明分组

  ```
  h1, h2, h3, h4, h5, h6 {
    color:gray;
    background: white;
    padding: 10px;
    border: 1px solid black;
    font-family: Verdana;
    }
  ```

- 类选择器

  语法是.加上类名，如.important

  - 类选择器允许以一种独立于文档元素的方式来指定样式

    该选择器可以单独使用，也可以与其他元素结合使用

    **只有适当地标记文档后，才能使用类选择器或者结合元素选择器**
  
  - ```
    <h1 class="important">
    This heading is very important.
    </h1>
    
    <p class="important">
    This paragraph is very important.
  </p>
    ```

    类选择器语法
  
    ```
  *.important {color:red;}
    ```

    如果您只想选择所有类名相同的元素，可以在类选择器中忽略通配选择器，这没有任何不好的影响：
  
    ```
    .important {color:red;}
    ```
    
  - 结合元素选择器，可以单独将段落显示为红色文本
  
    ```
    p.important {color:red;}
    ```
  
  - 多类选择器
  
    ```
    <p class="important warning">
    This paragraph is a very important warning.
    </p>
    ```
  
    多类两个词的顺序无关紧要，写成 warning important 也可以
  
    我们假设 class 为 important 的所有元素都是粗体，而 class 为 warning 的所有元素为斜体，class 中同时包含 important 和 warning 的所有元素还有一个银色的背景 。就可以写作：
  
    ```
    .important {font-weight:bold;}
    .warning {font-style:italic;}
    .important.warning {background:silver;}
    ```
  
- ID选择器

  一般情况下ID不应该被应用于样式，始终考虑使用class

  ID选择器是唯一的，同一个HTML文档中会且仅会生效第一次

  ID 选择器前面有一个 # 号，即# 加上id名

  ```
  #intro {font-weight:bold;}
  ```

  以下是一个实际 ID 选择器的例子：

  ```
  <p id="intro">This is a paragraph of introduction.</p>
  ```

- 请注意，类选择器和 ID 选择器可能是区分大小写的。所以类和 ID 值的大小写必须与文档中的相应值匹配。

- 属性选择器

  - **属性选择器可以根据元素的属性及属性值来选择元素**

  - 语法为元素名加上[该元素属性名]，例如以下

  - ```
    a[href] {color:red;}
    ```
  
- 后代选择器

  **后代选择器可以选择作为某元素后代的元素**，注意子元素孙元素都属于后代元素

  举例来说，如果您希望只对 h1 元素中的 em 元素应用样式，可以这样写：

  ```
  h1 em {color:red;}
  ```

  #### 语法解释

  在后代选择器中，规则左边的选择器一端包括两个或多个用空格分隔的选择器。选择器之间的空格是一种结合符（combinator）。因此，h1 em 选择器可以解释为 “作为 h1 元素后代的任何 em 元素”。

- 子元素选择器

  只选择某个元素的子元素，请使用子元素选择器（Child selector）。

  **注意，孙元素不属于子元素**

  例如，如果您希望选择只作为 h1 元素子元素的 strong 元素，可以这样写：

  ```
  h1 > strong {color:red;}
  ```

  这个规则会把第一个 h1 下面的两个 strong 元素变为红色，但是第二个 h1 中的 strong 不受影响：因为第二个h1中的strong是em的子元素，而不是h1的子元素

  ```
  <h1>This is <strong>very</strong> <strong>very</strong> important.</h1>
  <h1>This is <em>really <strong>very</strong></em> important.</h1>
  ```

- 相邻兄弟选择器

  选择紧接在另一个元素后的元素，而且二者有相同的父元素，可以使用相邻兄弟选择器（Adjacent sibling selector）。

  例如，如果要增加紧接在 h1 元素后出现的段落的上边距，可以这样写：

  ```
  h1 + p {margin-top:50px;}
  ```

  用一个结合符(+)只能选择两个相邻兄弟中的第二个元素

- 伪类  （pseudo：伪装的）

  伪类的语法如下，语法特征为冒号"  : "

  ```
  selector : pseudo-class {property: value}
  ```

  a:hover{color:red;} 

- 伪元素  （pseudo：伪装的）

  伪元素的语法：

  ```
  selector:pseudo-element {property:value;}
  ```



# CSS的属性

- list-style 简写属性在一个声明中设置所有的**列表**属性
- css图片截取，即截取大图片的某个区块进行显示，避免多次与服务器通信获取多张小图片



# CSS的框模型（Box Model）

- CSS 框模型 (Box Model) 规定了元素框处理元素内容、内边距、边框 和 外边距 的方式

  - （element）元素内容：元素框的最内部分是实际的内容。
  - （padding）内边距：直接包围内容的是内边距。内边距呈现了元素的背景。
  - （border）边框：内边距的边缘是边框。
  - （margin）外边框：边框以外是外边距，外边距默认是透明的，因此不会遮挡其后的任何元素。

  **提示：**背景应用于由内容和内边距、边框组成的区域。

  内边距、边框和外边距都是可选的，默认值是零。但是，许多元素将由用户代理样式表设置外边距和内边距。可以通过将元素的 margin 和 padding 设置为零来覆盖这些浏览器样式。这可以分别进行，也可以使用通用选择器对所有元素进行设置：

  ```
  * {
    margin: 0;
    padding: 0;
  }
  ```

  在 CSS 中，width 和 height 指的是内容区域的宽度和高度。增加内边距、边框和外边距不会影响内容区域的尺寸，但是会增加元素框的总尺寸。



# CSS框类型

- 具体见w3school教程中的CSS定位概述一节

  - 相对定位
    - **设置为相对定位的元素框会偏移某个距离。元素仍然保持其未定位前的形状。**
    - **它原本所占的空间仍保留（即仍旧保持原来的大小和形状）。**
  - 绝对定位
    - **设置为绝对定位的元素框从文档流完全删除，并相对于其包含块定位，包含块可能是文档中的另一个元素或者是初始包含块。**
    - **元素原先在正常文档流中所占的空间会关闭，就好像该元素原来不存在一样。**
    - **元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。**
  - 浮动
    - **浮动的框可以向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止。**
    - **由于浮动框不在文档的普通流中，所以文档的普通流中的块框表现得就像浮动框不存在一样。**

- #### 一切皆为框

  - div、h1 或 p 元素常常被称为块级元素。这意味着这些元素显示为**一块内容**，即“块框”。
  - 与之相反，span 和 strong 等元素称为“行内元素”，这是因为它们的内容显示在行中，即“行内框”。对行内框设置width 和 height 都不生效。

  可以使用 display 属性改变生成的框的类型。

- #### CSS 定位机制

  CSS 有三种基本的定位机制：普通流、浮动和绝对定位。

  浮动和绝对定位都会将元素从普通流中完全删除，**元素原先在正常文档流中所占的空间会关闭，就好像该元素原来不存在一样。**

  除非专门指定，否则所有框都在普通流中定位。也就是说，普通流中的元素的位置由元素在 (X)HTML 中的位置决定。

  - 块级框从上到下一个接一个地排列，框之间的垂直距离是由框的垂直外边距计算出来。

  - 行内框在一行中水平布置。可以使用水平内边距、边框和外边距调整它们的间距。但是，垂直内边距、边框和外边距不影响行内框的高度。由一行形成的水平框称为*行框（Line Box）*，行框的高度总是足以容纳它包含的所有行内框。不过，设置行高可以增加这个框的高度。

  在下面的章节，我们会为您详细讲解相对定位、绝对定位和浮动。

- #### DIV标签

  - \<div>标签可以定义文档中的分区或节(division/section)
  - \<div>标签可以把文档分割为独立的、不同的部分。它可以用作严格的组织工具，并且不使用任何格式与其关联
  - \<div>是一个块级元素，换行是\<div>固有的唯一格式表现
  - 可以将多个\<div>标签完全重叠为一个面，通过z-index属性设置沿着z轴的位置，正数离用户近，负数离用户远，从而实现翻书的效果




# Javascript

- 所有 JavaScript **标识符**对大小写敏感

- 单行注释以 // 开头,多行注释以 /* 开头，以 */ 结尾

- 在 HTML 中，JavaScript 代码必须位于 \<script> 与 \</script> 标签之间。

  ##### 实例

  ```
  <script>
  document.getElementById("demo").innerHTML = "我的第一段 JavaScript";
  </script>
  ```

- 脚本可被放置与 HTML 页面的\<body> 或 \<head> 部分中，或兼而有之

- 外部脚本：脚本可放置与外部文件中，在 \<script> 标签的 src (source) 属性中设置脚本的名称：

  ##### 实例

  ```
  <script src="myScript.js"></script>
  ```

- JavaScript 会忽略多个空格

- 关键字var用来定义变量

- 关键字function用来定义函数

  - ```
    function myFunction() {
        document.getElementById("demo").innerHTML = "Hello Kitty.";
        document.getElementById("myDIV").innerHTML = "How are you?";
    }
    ```

  - （）用来放置参数，{}用来放置语句

- this关键字在Javascript中的不同
  - 面向对象语言中，this关键字表示当前对象的一个引用
  - 而在Javascript中
    - 在对象方法，this表示该方法所属的对象
    - 直接使用，this表示全局对象
    - 在函数中，this表示全局对象
    - 在事件中，this表示接收事件的元素
    - 类似call()和apply()方法可以将this引用到任何对象，具体见实训邦：B站最全的《零基础入门学习Web前端》（适合完全小白/HTML/CSS/JS/Vue）P16的结尾部分



