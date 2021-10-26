#################################### 函数 ###################################

#### 内置函数 ####
# 例： int(), float(), str(),abs()
'''
t = int('12')
print(t)
'''


#### 自定义函数 ####
'''def语句，依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，函数的返回值用return语句返回'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# pass 占位符, 没有return，则返回return Null, 等价于return
def func():
    pass

# python解析器会做参数个数检查，不会做参数类型检查
'''数据类型检查可以用内置函数isinstance(),
类型不正确可使用raise抛出异常
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
'''
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 返回多个值, 可有默认参数
# 给出坐标、位移和角度，算出新的坐标：
# x, y = move(100, 100, 100 * math.sqrt(2) , -math.pi / 4)
# 此时返回的是一个tuple, 也可用tuple的访问方式访问返回值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#小结
'''
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。
'''



#### 函数的参数 ####
'''
Python 函数参数根据使用情况的不同需要分为 Argument 和 Parameter 两部分
'''
### I.Argument
'''
Argument 指的是函数调用时的实际参数，即实参
Python 中有两种 Argument，分别是「位置参数」和「关键字参数」
'''
## 1.位置参数 [positional argument]
def powder1(x, n):
    s = 1;
    while n > 0:
        s *= x
        n = n - 1  #n-- 语法错误 --n正确(这里的-表示负号)#
    return s
'''
powder(x, n)有两个参数x, n，这两个参数都是位置参数，
调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
powder(2,3)
powder(*(2,3))
*表示将可迭代对象扩展为函数的参数列表(尽量不要使用字典，因为传过去的是key)
'''

## 2. 关键字参数 [keyword argument]

'''
关键字参数使用时需要用标识符指明（name= 的形式），
或是以一个带有 ** 前缀的字典表示
powder(n=1,x=2)
powder(**{'n':1,'x':2})

注意：关键字参数必须在位置参数后面!
powder(x=1,2) SyntaxError: positional argument follows keyword argument
'''

## 补充：实参为可变数据类型时，实参会随形参的改变而改变
def changeme1(mylist):
    mylist.append([1,2])
    print("函数内取值",mylist)
    return


### II.Parameter
'''
Parameter 指的是函数定义时的形式参数，即形参 (formal parameter)。
Python 中有五种 Parameter，分别是「位置或关键字参数」、「仅位置参数」、
「仅关键字参数」、「可变位置参数」、「可变关键字参数」
'''

## 1.位置或关键字参数 [positional-or-keyword]
'''
位置或关键字参数在函数调用时可以以位置参数 (positional argument)
或关键字参数 (keyword argument) 的形式提供。它是默认的参数类型。
'''
def powder2(x, n=2):
    s = 1;
    while n > 0:
        s *= x
        n = n - 1
        return s
'''非默认参数(关键字参数)必须在默认参数(位置参数)后面!'''

## 2.仅位置参数 [positional-only]
'''
仅位置参数在函数调用时只能由位置参数 (positional argument) 提供。
Python 没有提供定义该参数的语法，它只在一些内置函数中存在，例如 abs()。
'''

## 3.仅关键字参数 [keyword-only]
'''
仅关键字参数在函数调用时只能由关键字参数 (keyword argument) 提供，
它可以对函数传入的关键字参数进行限制。
仅关键字参数定义时需要在其之前紧邻一个可变位置参数或增加一个特殊分割符 *.
'''
def person(name, age, *, city, job):
    print(name, age, city, job)
'''
person('tom', 23, city='wu', job='python')
person('tom', 23, **{'city':'wu', 'job':'python'})
错误形式
person('tom', 23,job='java')
'''
'''仅关键字参数设置默认值:person2('tom', 23, job='python')'''
def person2(name, age, *, city='ShangHai', job):
    print(name, age, city, job)
'''可变位置参数: person3('tom', 23, 34, city='wu', job='python')'''
def person3(name, age, *extra, city, job):
    print(name, age, extra, city, job)


## 4.可变位置参数 [var-positional]
'''
和java， c/c++中一样，用形似 *args 来表示
'''
def test_arg1(*arg):
    print(arg)
'''
*表示将函数调用时的多个参数打包成一个元组: test_arg(12,34)
传入0到任意多个到参数中，在函数调用时会自动被认为是一个元组
'''

## 5.可变关键字参数 [var-keyword]
'''
用形似 **kwargs 表示，可以传入0到任意多个“关键字-值”，
参数在函数内部被当做一个字典
'''
def test_kwargs(**kwargs):
    print(kwargs)
'''
** 表示将函数调用时的多个关键字参数打包成一个字典:
test_kwargs(name='tom', age=23)
test_kwargs(**{'name':'tom', 'age':23})
'''

## 6.Parameter 组合使用
'''
注意顺序
位置或关键字参数-非默认参数 > 位置或关键字参数-默认参数 > 可变位置参数
> 仅关键字参数 > 可变关键字参数
'''
def fun1(a, b=0, *arg, c=2, d,**kwargs):
    pass
'''
a:位置或关键字参数-非默认参数 b:位置或关键字参数-默认参数
arg: 可变位置参数 c,d:仅关键字参数, kwargs: 可变关键字参数
fun1(12, d='ew', key=12,t=34)
fun1(12,34,'arg1','arg2', c=12,d=34,ks1='kwargs1',ks2='kwargs2')
fun1(12,34, *('arg1','arg2'),c=12,d=34,**{'ks1':'kwargs1','ks2':'kwargs2'})
'''

## 补充：如果要使用非不变对象做默认参数，可借助不变变量None实现
'''
默认参数必须指向不变对象！否则会动态改变默认值
'''
def default_fun1(L=[]):
    L.append('END')
    return L
'''
如果要使用非不变对象做默认参数，可借助不变变量None实现
'''
def default_fun2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
