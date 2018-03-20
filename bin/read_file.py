import config.config
import os

filename = config.config.DATA_PATH+"trail-sample"
f = open(filename)
for line in f:
    temp = line.strip().split("\t")
    print(temp)

os.system("iconv -f GB18030 -t UTF-8 " \
          + config.config.DATA_PATH + os.path.basename("trail-sample") + " | sed 's/\t/,/g' > " \
          + config.config.DATA_PATH + \
          "/new-trail.csv")