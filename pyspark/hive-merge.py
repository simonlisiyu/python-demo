import sys
from pyspark import SparkContext,SparkConf
from pyspark.sql import *
# reload(sys)
# sys.setdefaultencoding('utf-8')

# conf = SparkConf()
# conf.setAppName('TTData')
# sc = SparkContext(conf=conf)
# sqlContext = HiveContext(sc)

#spark-submit merge.py its tide_tmc_daily_dii "\t" "city_id=15 and date_time='20171031'" /user/its_bi/lisiyu/tide
# database = sys.argv[1]
# table = sys.argv[2]
# table_split = sys.argv[3]
# where_condition = sys.argv[4]
# output_dir = sys.argv[5]
#
# print(database + "." + table + ":" + table_split)
# print("where = "+where_condition)
# print("output_dir = "+output_dir)

# sqlContext.sql("use "+database)
# dataDF = sqlContext.sql("select * from "+table+" where "+where_condition)
#
# sqlContext = SQLContext(sc)
# result = dataDF.rdd.repartition(1).map(lambda row: ','.join([str(c) for c in row]))
# print(result.first())
# result.saveAsTextFile(output_dir)

# $example on:manual_load_options$
input_dir = sys.argv[1]
table_split = sys.argv[2]
output_dir = sys.argv[3]

print(input_dir)
print("table_split = "+table_split)
print("output_dir = "+output_dir)

spark = SparkSession.builder.appName("TTData").getOrCreate()
df = spark.read.load(input_dir, format="text")
df.select("name", "age").write.save("namesAndAges.parquet", format="text")

spark.stop


