################################## 高级特性 ##################################

#### 切片 ####
'''
取lis或tuple的部分元素
传统方式：
取前3个
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L)
print([L[0], L[1], L[2]])

'''
若取前n个元素，就需要用循环了，显得繁琐
python提供了切片(slice)操作符，可对列表(list)，元组(tuple)，字符串进行裁剪操作
格式：L[begin:end:val], begin开始位置，end结束位置，每val个取一个元素,此三者均可不提供值
begin是操作对象的第一个元素
end是操作对象的最后一个元素
val是1
'''
print(L[0:3], end=' 取前三个\n')         # 不包含L[3]
print(L[-3:], end=' 取后三个\n')         # end, 结束符
print(L[1:4], end=' 取第二到第四个\n')
print(L[:]  , end=' 取所有\n')
print(L[:-2:2])

#### 列表生成式 ####
'''
从序列创建列表的简单途径。操作序列，用其获得的结果作为生成新列表的元素，
或者根据确定的判定条件创建子序列
列表生成式：
生成的元素放到前面，后面跟for子句，然后有零到多个 for 或 if 子句。
'''
# 平方序列 零个 for 或 if 子句
[x * x for x in range(1, 10)]

# 'ABC'和'EDF'全排列 一个 for 子句
[m.lower() + n.lower() for m in 'ABC' for n in 'EDF']

# 'ABC'和'EDF'全排列 排除'BD'
[m + n for m in 'ABC' for n in 'EDF' if m + n != 'BD']

# 'ABC'和'EDF'全排列，子元素用元组表示
[(m, n) for m in 'ABC' for n in 'EDF']

#### 生成器 ####
'''
一次生成一个值的特殊类型函数
并没有把所有的值存在内存中，而是在运行时生成值
创建生成器有两种方式
'''

# 方式一：只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(2)]
g = (x * x for x in range(2))
next(g)  #通过next()函数可获得generator的下一个返回值
'''
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
'''
for x in g:
    print(x)

'''如果用算法较为复杂，用类似列表生成式的创建方式无法实现时，还可用函数实现'''
# 方式二：有yield语句的函数是生成器
'''斐波拉契数列: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
'''
a, b = b, a + b 是python中的一种赋值方式
相对于;
t = b, a + b #t是元组
a = t[0]
b = t[1]
'''
for x in fib(5):
    print(x)
'''
不会执行while循环外面的语句(即return语句)
一是改return为yield
二是使用next，捕获StopInteration错误,返回值包含在StopIteration的value中
'''
g = fib(5)
while True:
    try:
        x = next(g)
        print(x, end=' ')
    except StopIteration as e:
        print(e.value)
        break

#### 迭代器 ####
'''
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
iter()用来生成一个迭代器
next()用来获取迭代器的下一个元素
'''
'''
可迭代(Iterable)类型数据都可通过iter()转化为迭代器
next()的参数必须是迭代器(Iterator)类型 #生成器是一种迭代器
判断方式如下：
'''
from collections.abc import Iterable
from collections.abc import Iterator
isinstance([], Iterable)
isinstance(iter([]), Iterator)

ite = iter(range(5))
type(ite)
next(ite)

'''
在loop.py中介绍过，凡是可用for遍历的数据均是Iterable类型，也就是说for循环可用
next()实现，其实Python的for循环本质上就是通过不断调用next()函数实现的
'''
for x in range(1,3):
    pass
#等价于
it = iter(range(1,3))  #获取迭代器对象
while True:            #循环
    try:           
        x = next(it)   #获取元素
    except StopIteration:
        break          #捕获StopIteration，退出循环


    
