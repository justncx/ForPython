# -*- coding: UTF-8 -*-
from random import randint
# 如何统计序列中元素出现的频度
# 案例描述：
'''
1、某随机序列【12,1,31,1,3，，，】中，找到出现次数最高的三个元素，它们出现的次数是多少
2、对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，它们出现的次数是多少
'''

data = [randint(0,20) for x in xrange(30)]
print data

c = dict.fromkeys(data,0)
print c
for x in data:
    c[x] += 1
print c