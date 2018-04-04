#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1. encode
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

# 2.ascii
print(chr(85))
print(ord("U"))

# 3.convert to int
print(int("a", 16))
print(int("0xa", 16))
print(int("10", 0)) #omitting the second parameter means to assume base-10
print(int("10", 10))
print(int("11", 2))

# 4. convert to hex
print(hex(1436331600))

'''
ord(x) Converts a single character to its integer value.

hex(x) Converts an integer to a hexadecimal string.

oct(x) Converts an integer to an octal string.

chr(x) Converts an integer to a character.

str(x) Converts object x to a string representation.

repr(x) Converts object x to an expression string.

eval(str) Evaluates a string and returns an object.

int(x [,base]) Converts x to an integer. base specifies the base if x is a string.

long(x [,base] ) Converts x to a long integer. base specifies the base if x is a string.

float(x) Converts x to a floating-point number.
'''

