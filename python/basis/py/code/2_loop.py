# for i = 1; i < 10; i++（语法错误）
#

for i in (1,2,3):
    print(i)



sum = 0
for x in range(101):
    sum = sum + x
print(sum)

'''
在python里，for不仅可以用于list,tuple,还可用于其它例如str等可迭代类型
可用for遍历的数据 <=> Iterable数据
判断一个对象是否可迭代
'''
'from collections import Iterable'
isinstance('abc', Iterable)


n = 0
while n <= 10:
    n = n + 1
    if n % 2 == 0:
        continue
    if n % 7 == 0:
        break
    print(n)
print('END')
