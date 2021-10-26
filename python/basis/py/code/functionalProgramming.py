################################## 函数式编程 ##################################
'''
简单说，"函数式编程"是一种"编程范式"（programming paradigm），也就是如何编写程序的方法论。
它属于"结构化编程"的一种，主要思想是把运算过程尽量写成一系列嵌套的函数调用
'''
'''
(1 + 2) * 3 - 4
　　var a = 1 + 2;
　　var b = a * 3;
　　var c = b - 4;


add(1,2).multiply(3).subtract(4)
'''

## 特性
# 1.闭包和高阶函数
'''
闭包是起函数的作用并可以像对象一样操作的对象
高阶函数可以用另一个函数（间接地，用一个表达式） 作为其输入参数，
在某些情况下，它甚至返回一个函数作为其输出参数。
'''

# 2.惰性计算
'''
表达式不是在绑定到变量时立即计算，而是在求值程序需要产生表达式的值时进行计算。
'''

# 3.递归
'''
用递归做为控制流程的机制
'''


## 特点
# 1. 函数是"第一等公民"
'''
所谓"第一等公民"（first class），指的是函数与其他数据类型一样，处于平等地位，可以赋值给其他变量，
也可以作为参数，传入另一个函数，或者作为别的函数的返回值。
'''

# 2. 只用"表达式"，不用"语句"
'''
"表达式"（expression）是一个单纯的运算过程，总是有返回值；"语句"（statement）是执行某种操作，没有返回值。函数式编程要求，
只使用表达式，不使用语句。也就是说，每一步都是单纯的运算，而且都有返回值。
'''

# 3.没有"副作用"
'''
"副作用"（side effect），指的是函数内部与外部互动，产生运算以外的其他结果。
（最典型的情况，就是修改全局变量的值）
'''

# 4.不修改状态
'''
函数式编程只是返回新的值，不修改系统变量
'''

# 5.引用透明性
'''
如果提供同样的输入，那么函数总是返回同样的结果
'''

'''
python部分支持函数式编程，例如：python没有代数数据类型或模式匹配，
也不支持尾调用优化等
'''
#### 高阶函数 ####
'''
reduce filter sorted内置的函数
'''
# map
'''
语法：map(function, iterable)
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''
def square(x):
    return x * x

sl = map(square, iter(range(1,5)))

def toStr(s):
    return str(s)

sl2 = map(toStr, iter(range(1,5)))
'''返回值是 map Iterable'''

# filter
'''
语法：filter(function, iterable)
用于过滤序列
把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
'''
def is_odd(n):
    return n % 2 == 1
 
fils = filter(is_odd, range(1,9))

# sorted
'''
语法：sorted(iterable, key=None, reverse=False)
函数对所有可迭代的对象进行排序操作
用sorted()排序的关键在于实现一个映射函数
'''
sorted([36, 5, -12, 9, -21], key=abs)
'''
key指定的函数会作用于iterable里的每个元素，并根据key函数返回的结果进行排序
'''

#### 函数作为返回值 ####
def lazy_add(x, y):
    z = 1
    def add():
        return (x + y) * z
    return add
'''
调用lazy_add()时，返回的并不是求和结果，而是求和函数，
在调用add时才会返回求和结果

'''
## 闭包 ##
'''
上述例子中，在lazy_add中定义了add，而且add函数使用lazy_add的参数和变量，
当lazy_add返回add时，相关参数和变量保存在返回的函数中，这种程序结构就称为闭包

闭包可以简单的理解为“定义在一个函数内部的函数“。
在本质上，闭包是将函数内部和函数外部连接起来的桥梁。
在使用闭包需注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量
'''
def cfunc():
    funcs = []
    for i in range(1,4):
        def func():
            return i * i
        funcs.append(func)
        print(func.__closure__[0].cell_contents)
    return funcs
'''
f1,f2,f3 = closure_func()
全部都是9！原因就在于返回的函数引用了变量i，但它(返回的函数)并非立刻执行,
而是在调用返回函数时执行，变量i的值是在外部函数结束时放在内部函数的__closure__里。
f1.__closure__[0].cell_contents（返回值是元组）

返回的函数执行时，是先从自己的__closure__里获取相关的变量值
f1.__closure__[0]，f2.__closure__[0]，f3.__closure__[0]，里面存放的int对象地址相同

__closure__里面放的不是变量值，而是变量的引用，也就是通过变量的引用获取变量的值

f1.__closure__[0].cell_contents = 9
f1() #81
'''
def cfunc1():
    funcs = []
    i = 1
    def func():
        return i * i
    funcs.append(func)
    i = 2
    print(funcs[0].__closure__[0].cell_contents)
    funcs.append(func)

    return funcs

'''
如果一定要使用会发生变化的变量：本质上类似于用n个变量来表示循环变量的n种变化
介绍两种处理方式
'''
# 1.借助函数：将内部函数放入数组时，就立即执行内部函数
'''(创建一个变量来存放循环变量的当前状态)'''
def cfunc2():
    funcs = []
    def func(j):
        def g():
            return j * j
        return g

    for i in range(1,4):
        funcs(func(i))
    return funcs

# 2.借助可迭代变量：用可迭代变量取代状态发生变化的变量，借助next()函数，动态改变参数
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
'''此时，函数__closure__中存放的是range(1,4)'''

#### 匿名函数 ####
'''
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
'''
# 特点：
'''
1.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
2.lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
'''
# 语法
'''
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''
lambda x, y: x * y

#### 装饰器 ####
def now():
    print('2019/10/12')
'''
假设我们要增强now()函数的功能，比如，在函数调用前自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
称之为“装饰器”（Decorator）。
'''
#import functools
def log(func):
    #@functools.wraps(func)
    def wrapper(*arg, **kw):
        print('call %s():'%func.__name__)
        return func(*arg, **kw)
    #wrapper.__name__ = func.__name__
    return wrapper

@log
def now():
    print('2019/10/12')
'''
func.__name__,获取函数名
wrapper.__name__ = func.__name__ <=> functools.wraps(func)

把@log放到now()函数的定义处，相当于执行了语句
now = log(now)
log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

'''
'''如果要使decorator自带参数，就要编写更复杂decorator'''
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

'''
@log('run')放到now()函数的定义处，相当于执行了语句
now = log('run')(now)
'''

#### 偏函数 ####

