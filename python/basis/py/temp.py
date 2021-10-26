sum = 0
for x in range(101):
    sum = sum + x
print(sum)

def gen():
    return (x for x in range(10))

'''
尾递归
f(n) = f(n-1) + f(n-2)
a=>f(n-2), b=>f(n-1)
'''
def fab(n, a, b):
  print("n=%s",n)
  if n <= 2:
      return b
  else:
      return fab(n-1, b, a + b)
'''
柯里化
里化（Currying）是把接受多个参数的函数变换成接受一个单一参数(最初函数的第一个参数)的函数，
并且返回接受余下的参数且返回结果的新函数的技术
'''
def currying(func, n):
    return lambda a = 1, b =1 , n: func(n, a, b)
def curried_fab(n) = currying(fab, n)

'''
迭代法：
'''
def fab2(n):
    a = 1
    b = 1
    while n > 2:
        a, b = b, a + b
        n = n -1
    return b


