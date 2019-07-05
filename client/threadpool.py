# -*-coding:utf-8-*-
# python 2.7
#  sudo pip install threadpool
__author__ = 'magicpwn'
import threadpool
import time, random
# worker 工作函数【多线程中每个线程工作的函数】
def worker_get(str):
    return str
# 回调函数，接受的参数（请求本身，和请求工作函数执行结果）可以省略
def print_result(request, result):
    print "the result is %s %r" % (request.requestID, result)
# data 设置为有20个随机1-10间的整数的列表，（列表中每一个数作为参数传递给工作函数运行一次）
data = [random.randint(1,10) for i in range(20)]
# 声明可容纳五个线程的池
pool = threadpool.ThreadPool(5)
# 创建线程运行内容请求列表（线程工作函数，线程工作参数列表，回调函数）
requests = threadpool.makeRequests(worker_get, data, print_result)
# 将每一个线程请求扔进线程池
[pool.putRequest(req) for req in requests]
# 等待data被消耗完，所有线程运行结束。
pool.wait()