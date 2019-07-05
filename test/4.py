#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import urllib2
import sys
import json


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, thread_num, order_id):
        threading.Thread.__init__(self)
        self.thread_num = thread_num
        self.order_id = order_id
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.thread_num
        get_order(thread_num, order_id)
        print "Exiting " + self.thread_num

def get_order(thread_num, order_id):
    contents = urllib2.urlopen("http://map-trafficft-warehouse-03.xg01:8080/traj/orderInfo?order_id="+order_id).read()
    print contents

filename = sys.argv[1]
f = open(filename)
threads = []
for line in f:
    obj = json.loads(line)
    for index in range(len(obj)):
        thread = myThread(index, obj[index])
        thread.start()
        threads.append(thread)

for t in threads:
    t.join()

print "Exiting Main Thread"