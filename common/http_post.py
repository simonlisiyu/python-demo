#! /usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, urllib

httpClient = None
try:
    #params = urllib.urlencode({"app_id":"xxxx", "sign":"yyyy", "timestamp":"12345","data":{"idc":"bj02123123","date":"2017-11-06"}})
    params = "{'metric':'trail.order', 'value':'yyyy', 'timestamp':'12345','tags':{'idc':'bj02022','date':'2017-11-08'}}"
    headers = {"Content-type": "application/json", "Accept": "text/plain"}

    httpClient = httplib.HTTPConnection("localhost", 4242, timeout=30)
    httpClient.request("POST", "/api/put?summary", params, headers)

    response = httpClient.getresponse()
    print(response.status)
    print(response.reason)
    print(response.read())
    print(response.getheaders()) #获取头信息
except Exception(e):
    print(e)
finally:
    if httpClient:
        httpClient.close()