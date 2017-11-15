# -*- coding: UTF-8 -*-
from collections import namedtuple
# 案例描述
'''
学生信息系统中数据为固定格式：
（名字，年龄，姓名，邮箱地址，。。。）

学生数量很大为了减小存储开销，对每个学生信息用元祖表示：
（'Jim',16,'male','jim1231@gmail.com'）
（'Lily',16,'female','Lily1231@gmail.com'）
（'JiK',16,'male','JiK1231@gmail.com'）
访问时，我们使用索引（index）来进行访问，大量索引降低程序可读性，
如何解决这个问题？？？

'''
# Eg：
student = ('Jim',16,'male','Jim12@163.com')

print student[0]
if student[1] <= 18:
    print "未成年"

# 这样写的话，代码的可读性和可维护性低
# 那么我们怎么做？？？

#方案一：定义类似于其他语言的美剧类型即定义常量
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
NAME,AGE,SEX,EMAIL = xrange(4)

print student[NAME]

# 方案二：使用标准库中的collections.namedtuple替代内置tuple
Student = namedtuple('Student',['name','age','sex','email'])
s = Student('Jim',16,'male','Jim@163.com')
print s.age
s1 = Student(name = 'jim', age=21, sex='male', email='Jim@163.com')
print s1.email