#在set中，没有重复的key,无序
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
#参数可以是列表，元组，字典等
de = '12'
s1 = {'df', de, '@#21'}
s2 = set(['df', 12, 'bsfg'])
s3 = set('ver')
print(s1)
print(s2)
print(s3)

#新增
s1.add(12)
print(s1)

#删除 key不存在时会报错 discard()
s1.discard(1)
print(s1)

#随机删除一个元素
s1.pop()
print(s1)
