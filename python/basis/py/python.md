# Python基础
## 简介
* Python 是著名的“龟叔”Guido van Rossum在1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言。

* Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。
```
Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。

Python 是交互式语言： 这意味着可以在一个 Python 提示符 >>> 后直接执行代码。

Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
```

## python安装
* python有两个版本，2.x和3.x，互不兼容
* 下载地址：https://www.python.org/downloads/
* 安装时勾选 add Python 3.7 to PATH


## 运行Python
编写python代码，我们会得到一个包含python代码的以`.py`为扩展名的文本文件。要运行代码，就需要Python解释器去执行.py文件。
* 命令行模式
* Python交互模式


## Python基础
* 编写python代码时，绝对不能用Word和Windows自带的记事本
* Python3.X 源码文件默认使用utf-8编码，指定编码格式：`# -*- coding: UTF-8 -*-` 或者 `# coding=utf-8`

> Python 标识符
* 标识符由字母、数字、下划线组成。
* 所有标识符可以包括英文、数字以及下划线( `_` )，但不能以数字开头
* Python 中的标识符是区分大小写的
<pre> 以下划线开头的标识符是有特殊意义的
<pre>
单下划线开头 _foo 的代表不能直接访问的类属性
双下划线开头的 __foo 代表类的私有成员
以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识
</pre></pre>

> 行和缩进
* Python中用`缩进`来控制代码块不是用`{}`

> 多行语句
* 斜杠（ `\` ）将一行的语句分为多行显示
```
total = item_one + \
        item_two
```

> Python 引号
* Python 可以使用引号( `'` )、双引号( `"` )、三引号( `'''` 或 `"""` ) 来表示字符串
* 其中三引号可以由多行组成，编写多行文本的快捷语法
```
text = '''hello
world
'''
```

> Python注释
* 单行注释采用 `#` 开头
* 多行注释使用三个单引号(`'''`)或三个双引号(`"""`)

> 输入输出
* print() <=> print(str, end='\n')
* input()


## 变量类型
> 变量赋值
* 变量赋值不需要声明类型
```
a = b
a = b = c = 1
a, b, c = 1, 2, "john"
```

> 标准数据类型
<pre>
Numbers（数字）
str（字符串）
list（列表）
tuple（元组）
dict（字典）
set（集合）
<pre>
不可变数据（3 个）：Number（数字）、str（字符串）、tuple（元组）
可变数据（3 个）：list（列表）、dict（字典）、set（集合）
除了Number（数字），其余的都是可迭代数据类型
</pre>
</pre>

> Numbers（数字）
* 支持 int、float、bool、complex（复数）
* * `long`也是用`int`表示
* * 判断`float`是否相等不要用 "`==`"
* * `bool, (True, False)`，布尔值可以用`and、or`和`not`运算
* * `complex`，可以用`a + bj`,或者`complex(a,b)`表示， 复数的实部`a`和虚部`b`都是浮点型
* * 数值运算：`**` 幂，`//` 取整除 - 向下取整
> str（字符串）
* Python中的字符串用单引号 `'` 或双引号 `"` 括起来，同时使用反斜杠( `\` )转义特殊字符。
```
'we\nare'
```
* 使用 `r` 可以让反斜杠不发生转义
```
r'we\nare'
```
* 字符串可以用 `+` 运算符连接在一起，用 `*` 运算符重复
```
'we' + 'are'
'we' * 2
```
* 字符串的格式化
* * 方式1，在Python中，采用的格式化方式和C语言是一致的，用 `%` 实现
<pre>
'Hi, I am %s. I am %d years old'%('klein', 24)
'%-4d-%05d' % (3, 1)
'%.2f' % 3.1415926
<pre>
常见的占位符有：
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
</pre></pre>
* * 方式2，使用 format()
```
'Hi, I am {0}. I am {1} years old'.format('klein', 24)
```

> list（列表）
* list是有序的、可重复的，可以随时添加和删除其中的元素。
* list元素类型没有限制
* 初始化, 语法: `L = [value1, value2...]`
```
classmates = ['Michael', 'Bob', '']
```
* 可用`len()`获得list长度
```
len(classmates)
```
* 访问
```
索引是从0开始, 以len(list) - 1 或-len(list)开始，-1结束
classmates[1]
classmates[len(classmates) - 1] 或 classmates[-1]
```
* 插入
```
classmates.append('Adam')       # 数组末尾插入
classmates.insert(1, 'Jack')    # 指定位置插入，1是索引位置
```
* 修改
```
classmates[1] = 'Sarah'
```
* 删除
```
classmates.pop()       # 数组末尾删除
classmates.pop(1)      # 指定位置删除，1是索引位置
```

> tuple（元组）
* tuple和list非常类似，但是tuple一旦初始化就不能修改
* 初始化, 语法: `L = (value1, value2...)`
```
classmates = ('Michael', 'Bob', 'Tracy')
classmates[0]
classmates[-2]
```
* tuple的元素存放的是元素的引用，不能更改引用，但可以更改元素的元素的值
```
classmates[1] = 12 #错误
L = [1,2]
tup = (1, L, 1)
tup[1][0] = 2
```

> dict（字典）
* dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
* 初始化, 语法：`d = {key1: value, key2: value...}`
```
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
```
* 访问
* * 方式1，`d[key]`
```
d['Bob']
```
* * 方式2，`dect.get(key)`
```
d.get('Bob')
```
* * 若没有查到，返回特殊值 `None`

* 新增或修改，`d[key] = value`
```
d['Bob'] = 70
d['Tom'] = 12
```
* 删除，`dect.pop(key)`
```
print(d.pop('Tracy'))
```
* 判断是否存在某个元素 `key in dect` (`in` 是成员运算符)
```
print('Tim' in d)
```

> set（集合）
* set是无序的，没有重复的
* 创建一个空集合必须用 `set()` 而不是 `{ }`，因为 `{ }` 是用来创建一个空字典
* 初始化，语法：`s = {key1, key2...}`
```
s1 = {'a', 'b', 'c'}
s2 = set(['v', 12, 'y'])   #set(Iterable)
```

* 新增, 语法：`set.add(key)`
```
s1.add(12)
```
* 删除
* * 方式1，语法：`set.remove(key)`, key不存在时会报错
```
s1.remove('df')
```
* * 方式2，语法：`set.discard(key)`, key不存在时不会报错
```
s1.discard(1)
```
* * 方式3，语法：`set.pop()`, 随机删除
```
s1.pop()
```

## 条件判断和循环
> 条件判断
* 每个条件后面要使用冒号 `:`，表示接下来是满足条件后要执行的语句块
* 使用 `缩进` 来划分语句块，相同缩进数的语句在一起组成一个语句块
* Python中没有switch – case语句
```
if condition_1:         # 只要condition是非零数值、非空str、非空list等，就判断为True，否则为False
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
```
height = 1.75
weight = 57
bmi = weight / (height * height)
if bmi < 18.5: 
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 25 and bmi < 28:
    print('肥胖')
else:
    print('严重肥胖')
```

> 循环
* 方式1，`for...in` 循环
```
for <variable> in <sequence>:  # sequence是可迭代类型
    <statements>
else:                          # 可选块，序列最后一个元素遍历完成时执行
    <statements>
```
```
for x in (1,2,3):
    print(1)
    if x == 3:
        break
else:
    print(2)
```
* * for i = 1; i < 10; i++（语法错误）
* * 判断一个变量是否可迭代
```
from collections.abc import Iterable
isinstance('abc', Iterable)
```
* 方式2，`while` 循环
```
while condition_1:
    statement_block_1
else:                     # 可选块，条件语句为 false 时执行 else 的语句块：
    statement_block_2
```
```
x = 3
while x > 1:
    print(x)
    x -= 1
else:
    print(-1)
```

## 函数
> 内置函数
* 例： int(), abs()，list(), map()等
```
int('12')
```

> 自定义函数
* Python 定义函数使用 `def` 关键字
```
def 函数名（参数列表）:
    函数体              # 缩进，返回值用return语句返回
```
```
def func(x):
    pass
```
* pass 占位符
* 若函数体中没有return语句，其结果为None, 等价于return None, 等价于return
* python解析器会做参数个数检查，不会做参数类型检查
* * 数据类型检查可以用内置函数 `isinstance()`
```
def func(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type') # 类型不正确可使用raise抛出异常
    else:
        return 0
```
* 可以返回多个值
<pre>
给出坐标、位移和角度，算出新的坐标
<pre>
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
</pre>
x, y = move(100, 100, 100 * math.sqrt(2) , -math.pi / 4)
此时返回的是一个tuple, 也可用tuple的访问方式访问返回值
</pre>

> 函数的参数 
* Python 函数参数根据使用情况的不同需要分为 Argument 和 Parameter 两部分
* I. Argument
```
Argument 指的是函数调用时的实际参数，即实参
Python 中有两种 Argument，分别是「位置参数」和「关键字参数」
```
* * 1.位置参数 [positional argument]
```
def powder(x, n):
    s = 1;
    while n > 0:
        s *= x
        n = n - 1  #n-- 语法错误 --n正确(这里的-表示负号)
    return s
```
```
x, n = 2, 5
powder(x, n)
powder(*(x,n))

powder(x, n)有两个参数x, n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
*表示将可迭代对象扩展为函数的参数列表(尽量不要使用字典，因为传过去的是key)
```

* * 2. 关键字参数 [keyword argument]
```
关键字参数使用时需要用标识符指明（name= value的形式），或是以一个带有 ** 前缀的字典表示
powder(n=1,x=2)
powder(**{'n':1,'x':2})

注意：关键字参数必须在位置参数后面!
powder(x=1,2)   # SyntaxError: positional argument follows keyword argument
```

* * 补充
```
实参为可变数据类型时，实参会随形参的改变而改变
def changeme(mylist):
    mylist.append([1,2])
    print("函数内取值",mylist)
    return

mylist = [8, 9]
changeme(mylist)
mylist
```

* II.Parameter
```
Parameter 指的是函数定义时的形式参数，即形参 (formal parameter)。
Python 中有五种 Parameter，分别是「位置或关键字参数」、「仅位置参数」、「仅关键字参数」、「可变位置参数」、「可变关键字参数」
```
* * 位置或关键字参数 [positional-or-keyword]
<pre>
位置或关键字参数在函数调用时可以以位置参数 (positional argument)或关键字参数 (keyword argument) 的形式提供。它是默认的参数类型。
<pre>
def powder2(x, n=2):
    s = 1;
    while n > 0:
        s *= x
        n = n - 1
        return s
</pre>非默认参数(关键字参数)必须在默认参数(位置参数)后面!</pre>

* * 仅位置参数 [positional-only]
```
仅位置参数在函数调用时只能由位置参数 (positional argument) 提供。
Python 没有提供定义该参数的语法，它只在一些内置函数中存在，例如 abs()。
```

* * 仅关键字参数 [keyword-only]
<pre>
仅关键字参数在函数调用时只能由关键字参数 (keyword argument) 提供，它可以对函数传入的关键字参数进行限制。
仅关键字参数定义时需要在其之前紧邻一个可变位置参数或增加一个特殊分割符 *.
<pre>
def person(name, age, *, city, job):
    print(name, age, city, job)
</pre>
person('tom', 23, city='wu', job='python')
person('tom', 23, **{'city':'wu', 'job':'python'})
错误形式
person('tom', 23,job='java')
</pre>

* * 可变位置参数 [var-positional]
* * * 和 java， c/c++中一样，用形似 `*args` 来表示, 传入0到任意多个到参数中，在函数调用时会自动被认为是一个元组
```
def test_arg1(*arg):      # *表示将函数调用时的多个参数打包成一个元组
    print(arg)

test_arg(12,34)
```

* * 可变关键字参数 [var-keyword]
* * * 用形似 `**kwargs` 表示，可以传入0到任意多个“关键字-值”，参数在函数内部被当做一个字典
```
def test_kwargs(**kwargs):   # ** 表示将函数调用时的多个关键字参数打包成一个字典
    print(kwargs)

test_kwargs(name='tom', age=23)
test_kwargs(**{'name':'tom', 'age':23})
```

* * Parameter 组合使用
<pre>
注意顺序: 
位置或关键字参数-非默认参数 > 位置或关键字参数-默认参数 > 可变位置参数
> 仅关键字参数 > 可变关键字参数
<pre>
def fun1(a, b=0, *arg, c=2, d,**kwargs):
    pass
</pre>
a:位置或关键字参数-非默认参数 b:位置或关键字参数-默认参数
arg: 可变位置参数 c,d:仅关键字参数, kwargs: 可变关键字参数<br>
fun1(12, d='ew', key=12,t=34)
fun1(12,34,'arg1','arg2', c=12,d=34,ks1='kwargs1',ks2='kwargs2')
fun1(12,34, *('arg1','arg2'),c=12,d=34,**{'ks1':'kwargs1','ks2':'kwargs2'})
</pre>

* * 补充：形参指向可变对象
```
默认参数必须指向不变对象！否则会动态改变默认值

def default_fun1(L=[]):
    L.append('END')
    return L
```
如果要使用可变对象做默认参数，可借助不变变量 `None` 实现
```
def default_fun2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

## 高级特性
> 切片
```
取list或tuple的部分元素

传统方式：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])

若取前n个元素，就需要用循环了，显得繁琐
```

* python提供了切片 (slice) 操作符，可对列表 (list)，元组 (tuple)，字符串进行裁剪操作
* 格式：`L[begin:end:val]`，begin开始位置，end 结束位置，每 val 个取一个元素, 此三者均可不提供值

默认值：begin 是操作对象的第一个元素, end 是操作对象的最后一个元素, val 是 1
```
print(L[0:3],   end=' 取前三个\n')         # 不包含L[3]
print(L[-3:],   end=' 取后三个\n')         # end, 结束符
print(L[1:4],   end=' 取第二到第四个\n')
print(L[:]  ,   end=' 取所有\n')
print(L[:-2:2], end=' 取第一个到倒数第二个，每两个取一个元素\n')
```

>  列表生成式
* 从序列创建列表的简单途径, 操作序列，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列
* 格式：`生成的元素放到前面，后面跟for子句，然后有零到多个 for 或 if 子句`
* 平方序列, `零个 for 或 if 子句`
```
[x * x for x in range(1, 10)]
```
* 'ABC'和'EDF' 全排列 `一个 for 子句`
```
m.lower() + n.lower() for m in 'ABC' for n in 'EDF']
```
* 'ABC'和'EDF'全排列 排除'BD' `一个 for 子句, 一个 if 子句`
```
[m + n for m in 'ABC' for n in 'EDF' if m + n != 'BD']
```
* 'ABC'和'EDF'全排列，子元素用元组表示
```
[(m, n) for m in 'ABC' for n in 'EDF']
```

> 生成器
```
使用了 yield 的函数被称为生成器（generator）
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
```
创建生成器有两种方式
* 方式一：只要把一个列表生成式的 `[]` 改成 `()`，就创建了一个generator
```
L = [x * x for x in range(2)]
g = (x * x for x in range(2))
next(g)           # 通过next()函数可获得generator的下一个返回值
```
generator保存的是算法，每次调用 `next(g)`，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出 `StopIteration` 的错误
* * generator的遍历
```
for x in g:
    print(x)
```
如果用算法较为复杂，用类似列表生成式的创建方式无法实现时，还可用函数实现

* 方式二：有 `yield` 语句的函数是生成器
```斐波拉契数列: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for x in fib(5):
    print(x)
```
* 不会执行 while 循环外面的语句 (即return语句)
* 需执行 while 循环外面的语句
* * 改 `return` 为 `yield`
* * 使用 `next()`，捕获 `StopIteration`，返回值包含在 `StopIteration.value` 中
```
g = fib(5)
while True:
    try:
        x = next(g)
        print(x, end=' ')
    except StopIteration as e:
        print(e.value)
        break
```

> 迭代器
* 迭代器是一个可以记住遍历的位置的对象
```
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：
iter() 和 next()。
iter()用来生成一个迭代器
next()用来获取迭代器的下一个元素
```
* * 可迭代 (`Iterable`) 类型数据都可通过 `iter()` 转化为迭代器
* * `next()` 的参数必须是迭代器 (`Iterator`) 类型
* 判断方式如下：
```
from collections.abc import Iterable
from collections.abc import Iterator
isinstance([], Iterable)
isinstance(iter([]), Iterator)

ite = iter(range(5))
type(ite)
next(ite)
```
* 遍历 Iterator，可用 for 循环<br>
`其实Python的for循环本质上就是通过不断调用next()函数实现的`<br>
```
it = iter(range(1,3)) # 获取迭代器对象
for x in it:
    print(x)

# 等价于

while True:            # 循环
    try: 
        x = next(it)   # 获取元素
        print(x)
    except StopIteration:
        break          # 捕获StopIteration，退出循环
```

## 函数式编程 
```
简单说，"函数式编程"是一种"编程范式"（programming paradigm），也就是如何编写程序的方法论。
它属于"结构化编程"的一种，主要思想是把运算过程尽量写成一系列嵌套的函数调用

(1 + 2) * 3 - 4
var a = 1 + 2;
var b = a * 3;
var c = b - 4;

add(1,2).multiply(3).subtract(4)
```

> 特性
* 1.闭包和高阶函数
```
闭包是起函数的作用并可以像对象一样操作的对象
高阶函数可以用另一个函数（间接地，用一个表达式） 作为其输入参数，在某些情况下，它甚至返回一个函数作为其输出参数。
```

* 2.惰性计算
```
表达式不是在绑定到变量时立即计算，而是在求值程序需要产生表达式的值时进行计算。
```

* 3.递归
```
用递归做为控制流程的机制
```

> 特点
* 1. 函数是"第一等公民"
```
所谓"第一等公民"（first class），指的是函数与其他数据类型一样，处于平等地位，可以赋值给其他变量，也可以作为参数，传入另一个函数，或者作为别的函数的返回值。
```

* 2. 只用"表达式"，不用"语句"
```
"表达式"（expression）是一个单纯的运算过程，总是有返回值；"语句"（statement）是执行某种操作，没有返回值。函数式编程要求，
只使用表达式，不使用语句。也就是说，每一步都是单纯的运算，而且都有返回值。
```

* 3.没有"副作用"
```
"副作用"（side effect），指的是函数内部与外部互动，产生运算以外的其他结果。（最典型的情况，就是修改全局变量的值）
```

* 4.不修改状态
```
函数式编程只是返回新的值，不修改系统变量
```

* 5.引用透明性
```
如果提供同样的输入，那么函数总是返回同样的结果
```
`python部分支持函数式编程，例如：python没有代数数据类型或模式匹配，也不支持尾调用优化等`

> 高阶函数
```
内置的函数: map filter sorted
```
* map
<pre>
语法：map(function, iterable)
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def square(x):
    return x * x

sl = map(square, iter(range(1,5)))
</pre>

* filter
```
语法：filter(function, iterable)
用于过滤序列, 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
    return n % 2 == 1
 
fils = filter(is_odd, range(1,9))
```

* sorted
```
语法：sorted(iterable, key=None, reverse=False)
函数对可迭代对象进行排序操作, 用sorted()排序的关键在于实现一个映射函数

sorted([36, 5, -12, 9, -21], key=abs)

key指定的函数会作用于iterable里的每个元素，并根据key函数返回的结果进行排序
```

> 函数作为返回值
```
def lazy_add(x, y):
    z = 1
    def add():
        return (x + y) * z
    return add

调用lazy_add()时，返回的并不是求和结果，而是求和函数，在调用add时才会返回求和结果
```

>  闭包
```
上述例子中，在lazy_add中定义了add，而且add函数使用lazy_add的参数和变量，
当lazy_add返回add时，相关参数和变量保存在返回的函数中，这种程序结构就称为闭包。

闭包可以简单的理解为“定义在一个函数内部的函数“。
在本质上，闭包是将函数内部和函数外部连接起来的桥梁。
```
```
在使用闭包需注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量

def cfunc():
    funcs = []
    for i in range(1,4):
        def func():
            return i * i
        funcs.append(func)
    return funcs

f1,f2,f3 = cfunc()
f1();f2();f3()

全部都是9！原因就在于返回的函数引用了变量i，但它(返回的函数)并非立刻执行, 而是在调用返回函数时执行。
变量i的引用放在内部函数的__closure__里。
f1.__closure__[0];f2.__closure__[0];f3.__closure__[0]，里面存放的int对象地址相同

f1.__closure__[0].cell_contents = 9
f1() #81
返回的函数执行时，是从__closure__里获取相关的参数值
```

* 如果一定要使用会发生变化的变量
```
处理点: 本质上类似于用n个变量来表示循环变量的n种变化，介绍两种处理方式
```
* * 1.借助函数：在将内部函数放入数组时，就立即执行内部函数
```创建一个变量来存放循环变量的当前状态
def cfunc2():
    funcs = []
    def func(j):
        def g():
            return j * j
        return g
    for i in range(1,4):
        funcs.append(func(i))
    return funcs
```

* * 2.借助可迭代变量：用迭代器变量取代状态发生变化的变量，借助 `next()` 函数，动态改变参数
```
def cfunc3():
    L = range(1,4)
    g = iter(L)
    funcs = []
    for i in L:
        def func():
            t = next(g)
            return t * t
        funcs.append(func)
    return funcs

此时，函数__closure__中存放的是range(1,4)
```

> 匿名函数
* python 使用 `lambda` 来创建匿名函数, 所谓匿名，即不使用 `def` 语句这样标准的形式定义一个函数。

* 特点：
```
1. lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
2. lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
```
* 语法
```
lambda 函数的语法只包含一个语句，如下：
lambda [arg1,arg2,.....argn]:expression

lambda x, y: x * y
```

> 装饰器
```
def now():
    print('2019/10/12')

假设我们要增强now()函数的功能，比如，在函数调用前自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
```
```
def log(func):
    def wrapper(*arg, **kw):
        print('call %s():'%func.__name__)
        return func(*arg, **kw)
    return wrapper

@log
def now():
    print('2019/10/12')

func.__name__,获取函数名
wrapper.__name__ = func.__name__ <=> functools.wraps(func)
functools.wraps(func) [import functools]

把@log放到now()函数的定义处，相当于执行了语句
now = log(now)
log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kwargs)，因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
```
```
如果要使decorator自带参数，就要编写更复杂decorator

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            print('%s %s():'%(text, func.__name__))
            return func(*arg, **kw)
        return wrapper
    return decorator

@log('run')
def now():
    print('2019/10/12')

@log('run')放到now()函数的定义处，相当于执行了语句
now = log('run')(now)
```

## 模块
> 在Python中，一个 `.py` 文件就称之为一个模块（Module）
```
我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。

import sys

此时就有了变量sys指向该模块

sys.path
```

* 如果一个只想导入一个模块的一部分
```
from collections.abc import Iterator
```

> 包（Package）是一种管理 Python 模块命名空间的形式，采用 "`点模块名称`"
```
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py

import mycompany.abc        # 必须使用全名去访问
mycompany.abc.printName()

from mycompany import abc   # 可直接用模块名访问
abc.printName()
```

* 注意的是：
```
1. 一个包必须有__init__.py，如果没有，python会认为它是一个普通的文件夹,
__init__.py可以是一个空文件夹，也可以存载pyhon代码
2. 模块名要遵循Python变量命名规范，不要使用中文、特殊字符
```

* 操作第三方模块<br>
第三方库一般都会在Python官方的pypi.python.org网站注册
```
在命令提示符窗口下运行pip

pip install pillow
pip show pillow
pip uninstall pillow
```

## 异常处理与调试
> 异常处理
* `try` 机制
```
try:                              try:
    代码块1               |            代码块1
except (异常1, 异常2):             except 异常1:
    代码块2               |            代码块2
else:         # 可选               except 异常1:
    代码块3               |            代码块3
finally:      # 可选
    代码块4               |
```
当没有错误发生时，会自动执行else语句
```
try:
    x = 4 / 0
except ZeroDivisionError as e:      # 捕获 ZeroDivisionError
    print('ZeroDivisionError:', e)
```
```
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    raise
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```
* * 有多个 except 时，若异常被前面的 except 捕获，后面的 except 将不再执行
* * 捕获异常时，不仅能捕获该类型的异常错误，还能捕获其子类的异常错误
* * 常见的错误类型和继承关系：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

* 抛出异常
* * Python 使用 `raise` 语句抛出一个指定的异常
```
def func(num):
    if not isinstance(num, int):
        raise TypeError('bad operand type')
```
* 自定义异常
* * 根据需要，可以定义一个 "异常" 的 class，选择好继承关系，然后，用 raise 语句抛出一个错误的实例 
```
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```

> 调试
* 程序能一次写完就正常运行的可能性很小，总是有各种各样的 bug 需要修复，一些复杂的 bug 看错误信息看不出来，要找到错误的变量，就需要看那些调试了
* `方式1`：用 `print()` 把变量打印出来
* `方式2`：断言（`assert`）
* * 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
* * 语法：
```
assert expression [, arguments]

等价于
if not expression:
    raise AssertionError(arguments)
```
```
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
```
* `方式3`：借助 python 模块 `logging` , 不会抛出错误，而且可以输出到文件
```
import logging
logging.basicConfig(level=logging.INFO)

logging.info('test info')
logging.debug('test debug')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')
```
* * 信息的级别: DEBUG, INFO, WARING, ERROR, CRITICAL

* `方式4`：启动Python的调试器 `pdb`
* * 让程序以单步方式运行，可以随时查看运行状态
* * 命令行模式启动 `python -m pdb err.py`
```
l : （list）列出源码
n : （next）执行下一条语句
p 变量名 : （print）输出expression的值
q : （quit）退出调试
```
* `方式5` : 借助 `pdb.set_trace()`
* * 此方法也是用pdb，但是不需要单步执行
```
import pdb

s1 = 12
s1 += 12
pdb.set_trace()
s2 = s1

运行pdb.set_trace(), 就会自动暂停，相对于加了一个断点，并进入pdb模式
```