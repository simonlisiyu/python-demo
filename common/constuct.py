
# 1.map字典的方法
map = {}
map["k1"] = "v1"
for kv in map.items():
    print(kv[0])
print(map.items())
print(map['k1'])
print(map.keys())     # 输出所有键
print(map.values())    # 输出所有值
del map["k1"]   # 删除键是'k1'的条目
'''
1	dict.clear()
删除字典内所有元素
2	dict.copy()
返回一个字典的浅复制
3	dict.fromkeys(seq[, val])
创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
4	dict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	dict.has_key(key)
如果键在字典dict里返回true，否则返回false
6	dict.items()
以列表返回可遍历的(键, 值) 元组数组
7	dict.keys()
以列表返回一个字典所有的键
8	dict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)
把字典dict2的键/值对更新到dict里
10	dict.values()
以列表返回字典中的所有值
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
随机返回并删除字典中的一对键和值。
'''

# 2.array数组的方法
array = ["222","333","444"]
array.append("111")
array[0] = "10"
print(array)
brr = array
brr += array
print(brr)
print(array[:2])
print(array[0])            # 输出列表的第一个元素
print(array[-2])            # 输出列表的倒数第二个元素
print(array[1:3])         # 输出第二个至第三个元素
print(array[2:])           # 输出从第三个开始至列表末尾的所有元素
print(array + array)           # 打印组合的列表

# 使用切片来删除
li = [1,2,3,4,5,6]
li = li[:-2]
print(li)

'''
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop(obj=list[-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort([func])
对原列表进行排序
'''

# 3.tuple元组的方法,元组是不允许更新的。而列表是允许更新的
tuple = ()
tuple += ("aaa", 1)
tuple += ("b", "2")
tuple += ("c", 3)
tuple += ("d", "4")
print(tuple)
print(tuple[0])            # 输出列表的第一个元素
print(tuple[1:3])         # 输出第二个至第三个元素
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tuple + tuple)           # 打印组合的列表

# 4.set集合的方法
x = set('spam')
y = set(['h','a','m'])
print(x,y)
print(x&y)  #交集 x.intersection(y)
print(x|y)  #并集 x.union(y)
print(x-y)  #差集 x.difference(y)
print(x^y)  #对称差集（项在x或y中，但不会同时出现在二者中） x.symmetric_difference(y)
x.add('f')            # 添加一项
x.update([10,37,42])  # 添加多项
print("xxx", x)
x.remove('f')   #从 set “x”中删除元素 f, 如果不存在则引发 KeyError
x.discard('f')  #如果在 set “x”中存在元素 f, 则删除
len(x)
's' in x    #测试 s 是否是 x 的成员
's' not in x    #测试 s 是否不是 x 的成员
y <= x      #等同y.issubset(x)， 测试是否 y 中的每一个元素都在 x 中
y >= x      # y.issuperset(x)
x.copy()    #返回 set “x”的一个浅复制

# 5.其他的集合应用方法
#去除海量列表里重复元素
arr1 = [11,22,33,44,11,22]
set1 = set(arr1)
print(set1)
arr2 = [i for i in set1]
print(arr2)

# 6.循环
# count = 0
# while count < 2:
#     print(count, " is  less than 2")
#     count = count + 1
# else:
#     print(count, " is not less than 2")
#
# for index in range(len(array)):
#     print('当前is :', array[index])
#
# for i in range(10):
#     print(i)
# # 倒叙
# for i in range(10)[::-1]:
#     print(i)

