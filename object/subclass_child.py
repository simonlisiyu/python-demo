#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
    __secretCount = 0  # 私有变量
    parentAttr = 100    # 公开变量

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)

    def myMethod(self):
        print('调用父类方法-重写')

class Child(Parent): # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')

    def myMethod(self):
        print('调用子类方法-重写')

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值

'''
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
'''