#!/usr/bin/python

import _thread
import urllib2
import sys
import json


def get_order(thread_num, order_id):
    contents = urllib2.urlopen("http://map-trafficft-warehouse-03.xg01:8080/traj/orderInfo?order_id="+order_id).read()
    print thread_num

filename = sys.argv[1]
f = open(filename)
for line in f:
    obj = json.loads(line)
    for index in range(len(obj)):
        try:
            _thread.start_new_thread(get_order, (index, obj[index]))
        except:
            print "Error: 无法启动线程"
        while 1:
            pass

print "finish."
