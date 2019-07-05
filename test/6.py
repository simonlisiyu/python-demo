import urllib
import urllib2
import json

url = "http://10.89.236.25:8086/api/traj/traj/list/gps"
#url = "http://100.69.238.158:8001/api/traj/traj/traj/list/gps"
body_value = {"polygon_range": "102.668697-25.071761,102.672817-25.057456,102.672130-25.033506,102.677366-25.033428,102.702257-25.017095,102.712900-25.016395,102.713415-25.011262,102.701312-25.012040,102.674791-25.028139,102.667753-25.027206,102.666809-25.033506,102.668182-25.056600,102.665178-25.071139","city_id": "19","start": "1530028800","end": "1530115200","size": "2","index":"1,2,3,8"  }
body_value  = urllib.urlencode(body_value)
request = urllib2.Request(url, body_value)
request.add_header("Content-Type", "application/x-www-form-urlencoded")
result = urllib2.urlopen(request,timeout=6000 ).read()

# e = json.loads(result)
# print type(e)
# print e['total']
#
# total_str = ""
# data = e['data']
# for i in range(0,len(data)):
#     print i
#     pointList = data[i]['pointList']
#     orderInfo = data[i]['orderInfo']
#     orderId = orderInfo[0]
#     p_str = orderId + "\t" + "none" + "\t"
#     for k in range(0,len(pointList)):
#         dataNo3 = ""
#         for j in range(0,len(pointList[k][3])):
#             dataNo3 = dataNo3 + str(pointList[k][3][j])+"|"
#         dataNo3Final = dataNo3[:-1]
#         p_str = p_str + str(pointList[k][0]) + "," + str(pointList[k][1]) + ","+ str(pointList[k][2])+ "," + dataNo3Final + ";"
#     total_str = total_str + p_str[:-1] + "\n"

f = open("./6.txt","w")
f.write(result)
f.close()