import sys
from pyspark import SparkContext,SparkConf
from pyspark.sql import *

conf = SparkConf()
conf.setAppName('TTData')
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

# 3.get link attr from hive
sqlContext.sql("use gulfstream_dwd")
df_link_info=sqlContext.sql("select order_id,city_id,driver_id,order_status,is_td_finish,begin_charge_time,"
                            "finish_time,starting_lng,starting_lat,dest_lng,dest_lat,"
                            "`year`,`month`,`day` from dwd_order_make_d where city_id=12 and year=2018 and month=04 and day=01")
df_link_info.registerTempTable("dwd_order_make_d_temp")
# sqlContext.cacheTable("link_attr_temp")

# rdd_link2city = sc.textFile(file_link2cityid).map(lambda line:line.split(' ')).map(lambda p:Row(linkid=p[0], provinceid=int(p[1]), cityid=int(p[2])))
# df1 = sqlContext.createDataFrame(rdd_link2city)
# df1.filter(df1.cityid == cityid).registerTempTable('link2city')

result = sqlContext.sql("select * from dwd_order_make_d_temp where city_id=12")

# result.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")

result.rdd.map(lambda row:[str(c) for c in row]).saveAsTextFile("/user/its_bi/lisiyu/order")

# provinceid = result.first()['provinceid']

# rdd_linkfreespeed = sc.textFile(file_linkfreeapeed).map(lambda line:line.split('\t')).map(lambda p:Row(linkid=p[0], freespeed=float(p[1])))
# sqlContext.createDataFrame(rdd_linkfreespeed).registerTempTable('linkfreespeed')
#
# file_linkspeed = "%s/%s/%s/%s/%s" % (dir_linkspeed,str(provinceid), dt[0:4], dt[4:6], dt[6:8])
# rdd_linkspeed = sc.textFile(file_linkspeed).map(lambda line:line.split(',')).map(lambda p:Row(dt=p[0], idx=p[1], linkid=p[2], speed=float(p[5]),length=int(p[8])))
# df2 = sqlContext.createDataFrame(rdd_linkspeed)
# df2.filter(df2.speed > 0).registerTempTable('linkspeed')
#
# #sqlContext.sql("select lw.linkid, 1 as weight, 1 as level, l.length, l.length/f.freespeed as tt, l.length/l.speed as tt_current, cast(substr(l.idx,1,2)*30+substr(l.idx,3,2)/2 as int) as idx_new from link2city lw, linkfreespeed f, linkspeed l where lw.linkid=f.linkid and f.linkid=l.linkid").coalesce(100).registerTempTable("result")
# sqlContext.sql("select l.linkid, 1 as weight, 1 as level, l.length, l.length/f.freespeed as tt, l.length/l.speed as tt_current, cast(substr(l.idx,1,2)*30+substr(l.idx,3,2)/2 as int) as idx_new from linkfreespeed f join linkspeed l on f.linkid=l.linkid").coalesce(100).registerTempTable("result")
#
# sqlContext.sql("use its")
# sqlContext.sql("insert overwrite table tti_by_link_tmp_new partition(dt='" + dt + "', cityid="+cityid+") " + " select * from result")
sc.stop()