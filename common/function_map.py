

def square(x) :            # 计算平方数
    return x ** 2

map_new = map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
map_new = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
map_new = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])  # 提供了两个列表，对相同位置的列表数据进行相加

# reduce
# def add(x, y) :            # 两数相加
#     return x + y
# reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
# reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数