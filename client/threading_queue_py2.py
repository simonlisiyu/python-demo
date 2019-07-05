# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import Queue
# import threading
# import urllib2
# import sys
# import json
# import time
#
# SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列
# _WORKER_THREAD_NUM = int(sys.argv[3])   #设置线程个数
#
# class MyThread(threading.Thread) :
#
#     def __init__(self, func) :
#         super(MyThread, self).__init__()
#         self.func = func
#
#     def run(self) :
#         self.func()
#
# def worker() :
#     global SHARE_Q
#     while not SHARE_Q.empty():
#         order_id = SHARE_Q.get() #获得任务
#         contents = urllib2.urlopen("http://xxx:8080/traj/orderInfo?order_id="+order_id).read()
#         #print contents
#         #print time.time()
#
# def main() :
#     global SHARE_Q
#     filename = sys.argv[1]
#     count = int(sys.argv[2])
#     f = open(filename)
#     obj = {}
#     for line in f:
#         obj = json.loads(line)
#         count = min(count, len(obj))
#         obj = obj[:count]
#
#     threads = []
#     for order_id in obj :  #向队列中放入任务
#         SHARE_Q.put(order_id)
#     for i in range(_WORKER_THREAD_NUM) :
#         thread = MyThread(worker)
#         thread.start()
#         threads.append(thread)
#     for thread in threads :
#         thread.join()
#
# if __name__ == '__main__':
#     print time.time()
#     main()
#     print time.time()
