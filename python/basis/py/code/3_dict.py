#字典
#查找速度都非常快，不会随着字典大小的增加而变慢,list会
# 内置函数: dict()创建字典。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#新增或更新
d['Bob'] = 70
d['Tom'] = 12
print(dict)

#查找，d[key] or d.get(key)
'''
d[key], key不存在，会报错
d.get(key), key不存在，返回None

'''
print(d['Michael'])
print(d.get('Bob'))
print(d.get('Thomas', '-1'))

#key是否存在于d
print('Tim' in d)

#删除，删除一个key，用pop(key)方法
print(d.pop('Tracy'))
print(d.get('Tracy'))
