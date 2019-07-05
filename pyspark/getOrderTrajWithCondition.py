import sys
from pyspark import SparkContext,SparkConf
from pyspark.sql import *

city_id = sys.argv[1]
year = sys.argv[2]
month = sys.argv[3]
day = sys.argv[4]
phone_prefix = sys.argv[5]
num = int(sys.argv[6])

spark = SparkSession \
    .builder \
    .appName("get order traj with condition") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("use gulfstream_dwd")
order_df = spark.sql("select o.driver_id,o.passenger_phone,o.begin_charge_time,o.finish_time,t.traj "
                     "from gulfstream_dwd.dwd_order_make_d o where city_id="+city_id+
                     " and year="+year+" and month="+month+" and day="+day+
                     " and is_td_finish=1 limit "+num+"left out join map_bi.map_match_driver_traj t")
order_df = spark.sql("select o.driver_id,o.passenger_phone,o.begin_charge_time,o.finish_time,t.traj "
                     "from gulfstream_dwd.dwd_order_make_d o left outer join map_bi.map_match_driver_traj t "
                     "on o.driver_id = t.user_id where ")
spark.sql("use map_bi")
trail_df = spark.sql("select user_id,traj from map_match_driver_traj where "
                     "year="+year+" and month="+month+" and day="+day)

