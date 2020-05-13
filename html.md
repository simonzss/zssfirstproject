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