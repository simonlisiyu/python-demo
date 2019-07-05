#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import sys
import json
import pymysql

reload(sys)
sys.setdefaultencoding('utf8')

# 0. init param
# filename = sys.argv[1]
# db_ip = sys.argv[2]
# db_port = sys.argv[3]
# db_user = sys.argv[4]
# db_pwd = sys.argv[5]
filename = "/Users/didi/Desktop/doc/2.部门文档/治堵平台/互联网警情/12_2018061212.txt"
db_ip = '10.95.96.91'
db_user = 'root'
db_pwd = 'root'
db_database = 'traffic'
date = '2018-04-30'

# 1. get road net version
url = "http://100.90.164.31:8001/signal-map/map/getDateVersion"
body = {"date": date}
body_value = urllib.urlencode(body)
request = urllib2.Request(url, body_value)
request.add_header("Content-Type", "application/x-www-form-urlencoded")
result = urllib2.urlopen(request, timeout=6000).read()
data = json.loads(result)
road_version = data['data'][date]
print "road_version"+road_version

# 2. get db connection
db = pymysql.connect(db_ip, db_user, db_pwd, db_database)
cursor = db.cursor()

# 3. open file and for data
f = open(filename)
for line in f:
    # 3.1 get file data, inlink...
    split = line.strip().split(' ')
    inlink = split[0]
    outlink = split[1]
    label = split[2]

    # 3.2 get geom of inlink
    url = "http://100.90.164.31:8001/signal-map/mapFlow/linkinfo?link_ids=%s&version=%s" % (inlink, road_version)
    print url
    try:
        contents = urllib2.urlopen(url, timeout=60).read()
    except:
        continue
    data = json.loads(contents)
    geom_sp = data['data']['links_info'][inlink]['geom'].replace(",", " ").split(";")
    print geom_sp
    geom = geom_sp[0] + "," + geom_sp[len(geom_sp) - 1]
    print geom

    # 3.3 insert data to db
    sql = """INSERT INTO lable_table(mline,
             link_id, tag_detail, roadnet_version)
             VALUES (ST_GEOMFROMTEXT('MULTILINESTRING((%s))'),
             '%s', '%s', '%s')""" % (geom, inlink, label, road_version)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    print inlink
    print sql

db.close()