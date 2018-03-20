#!/usr/bin/python

import json

data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

# Python 字典类型转换为 JSON 对象
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 写入 JSON 数据
with open('../data/data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('../data/data.json', 'r') as f:
    data = json.load(f)
    print(data)