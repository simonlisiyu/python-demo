#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
import sys


def send_json(json, s):
    print(json)
    r = s.post("http://localhost:4242/api/put?details", json=json)
    print(r.text)
    return r.text


fileprefix = "/Users/Documents/"
s = requests.Session()

for i in range(1, len(sys.argv)):
    print(sys.argv[i])
    array = []
    f = open(fileprefix+sys.argv[i])
    for line in f:
        temp = line.strip().split("\t")
        json = {
            "metric": "trail.order",
            "timestamp": int(temp[0]),
            "value": float(temp[1]),
            "tags": {
                "oid": temp[2],
                "od": temp[3],
                "hour": int(temp[4])+1,
                "weekday": temp[5],
                "month": temp[6],
                "isholiday": temp[7],
                "linkids": temp[8].replace(",", "/"),
                "junctionid": temp[9],
                "roadid": temp[10],
                "cityid": temp[11]
            }
        }
        array.append(json)
        if len(array) == 20:
            print("array="+array.__str__())
            send_json(array, s)
            array = []
            # break
    if len(array) != 0:
        send_json(array, s)
        array = []
print("finish.")




