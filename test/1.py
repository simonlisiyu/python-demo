#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import sys
import json

# contents = urllib2.urlopen("http://map-trafficft-warehouse-03.xg01:8080"
#                            "/traj/areaOrders?"
#                            "lb=116.201520,39.751710"
#                            "&ru=116.218214,39.764808"
#                            "&st=1523330253&et=1524110002"
#                            "&limit=10").read()

filename = sys.argv[1]
f = open(filename)
links = []
for line in f:
    link = line.strip().split('\t')[0]
    links.append(link)

linkStr = ','.join(links)
print linkStr
url = "http://map-trafficft-warehouse-03.xg01:8080"\
      +"/traj/linkOrders?"\
      +"links="+linkStr\
      +"&map_version=2018011219"\
      +"&st=1519833600&et=1522425600"\
      +"&limit=100000"
print url
contents = urllib2.urlopen(url).read()

data = json.loads(contents)
print len(data)
print data[0]