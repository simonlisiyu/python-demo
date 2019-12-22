import lib.mysql as mydb

db = mydb.DB()
db.connect(
    {
        'host': '100.90.164.31',
        'port': 3306,
        'user': 'root',
        'passwd': '',
        'database': '',
    })

sql = "select nodeid1, nodeid2, level, next_linkids from link_%s where linkid=%s" % ('20170412', '343434')
res = db.select(sql)
{'snodeid': res[0]['nodeid1'], 'enodeid': res[0]['nodeid2'], 'level': res[0]['level'],
        'next_linkids': res[0]['next_linkids'].strip(',').split(',')}

ql = "select linkid,nodeid1, nodeid2, length,level,kind,next_linkids,lanenum from link_%s where nodeid1 in (%s)" % (
    '20170412', 'nodeid')
res = db.select(sql)
linkinfo = {}
for i in res:
    linkinfo[str(i['linkid'])] = {'length': i['length'], 'level': i['level'], 'kind': i['kind'],
                                  'next_linkids': i['next_linkids'].strip(',').split(','), 'snodeid': i['nodeid1'],
                                  'enodeid': i['nodeid2']}

db.disconnect()