# -*- coding: UTF-8 -*-
from random import randint
import timeit
# 如何在列表，字典，集合中根据条件来筛选数据
# 通用做法：：
data = [1,5,-3,2,-6,9]
res = []
for x in data:
    if x >= 0 :
        res.append(x)
print res

#在Python中我们怎么做?
# 1、使用filter函数
data = [randint(-10,10) for x in xrange(10)]
print data

data = filter(lambda x: x >= 0 ,data)
print data

# 2、使用列表解析的方法
data = [randint(-10,10) for x in xrange(10)]
print data
data = [x for x in data if x >= 0]
print data

# time = timeit.timeit(filter(lambda x: x>= 0,data))

# 对于字典筛选出某些元素
d = {x: randint(60,100) for x in range(1,21)}
print d
# 字典解析
d = {k: v for k,v in d.iteritems() if v > 90}
print d

# 对于集合中筛选出某些元素
# 集合解析

data = [randint(-10,10) for x in range(10)]
s = set(data)
print s
s = {x for x in s if x % 3 == 0}
print s