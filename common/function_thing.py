#!/usr/bin/python
# -*- coding: UTF-8 -*-

#缺省参数
def printinfo( name, age = 35 ):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return

#不定长参数
def printinfo2( arg1, *vartuple ):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

#lambda函数
sum = lambda arg1, arg2: arg1 + arg2;

#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )

printinfo2( 10 )
printinfo2( 70, 60, 50 )

print("相加后的值为 : ", sum( 10, 20 ))

# abs
print("abs(-45) : ", abs(-45))
# divmod, 把除数和余数运算结果结合起来，返回一个包含商和余数的元组
print(divmod(7, 2))
# all any, 元素是否 全不/全 为 0、''、False 或者 iterable 为空
print(all(('a', 'b', 'c', 'd')))
print(all((0, 1, 2, 3)))
print(any([0, '', False]))        # 列表list,元素全为0,'',false
print(any(['a', 'b', '', 'd']))   # 列表list，存在一个为空的元素
# enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))       # 小标从 1 开始
# ord,返回对应的 ASCII 数值，或者 Unicode 数值 十进制整数
print(ord('a'))
# isinstance
print(isinstance(5,int))
# bin() 返回一个整数 int 或者长整数 long int 的二进制表示
print(bin(10))

# filter
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(set(newlist))

# range
print(range(0, 30, 5))
print(range(0, 3))

# format
"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.abc.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.abc.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# getattr
class A(object):
    bar = 1
a = A()
getattr(a, 'bar')        # 获取属性 bar 值

# cmp, python 2.7, 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# print("cmp(80, 100) : ", cmp(80, 100))
# operator 模块，适合任何对象
import operator
a = 'hello'
b = 'name'
operator.lt(a, b)
operator.le(a, b)
operator.eq(a, b)
operator.ne(a, b)
operator.ge(a, b)
operator.gt(a, b)
operator.__lt__(a, b)
operator.__le__(a, b)
operator.__eq__(a, b)
operator.__ne__(a, b)
operator.__ge__(a, b)
operator.__gt__(a, b)

# zip
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)     # 打包为元组的列表,[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式, [(1, 2, 3), (4, 5, 6)]

# round, 方法返回浮点数x的四舍五入值。
print("round(80.23456, 2) : ", round(80.23456, 2))

# hash, 用于获取取一个对象（字符串或者数值等）的哈希值。
hash('test')            # 字符串

# next
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

# sorted
a = [5,7,6,3,4,1,2]
b = sorted(a)       # 保留原列表
L=[('b',2),('a',1),('c',3),('d',4)]
sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
sorted(L, key=lambda x:x[1])               # 利用key
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2], reverse=True)       # 按降序