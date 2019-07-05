
def getSegs(rows):
    array = []
    split_flag = 1 #0=last not junction, other last is junction
    for row in rows:
        print()
        print()
        print(row)
        if len(array) == 0:
            print("1")
            array.append([row])

            print(array)
            print(len(array))
            print(array[0])
        elif row['cross_flag'] != 0 and split_flag == 0:
            print("2")
            split_flag = row['cross_flag']
            array.append([row])
            print(array)
        else:
            print("3")
            split_flag = row['cross_flag']
            array[len(array)-1].append(row)
            print(array)
    return array


row1 = {}
row2 = {}
row3 = {}
row1["k1"] = "v1"
row2["k1"] = "v2"
row3["k1"] = "v3"
row1["cross_flag"] = 1
row2["cross_flag"] = 1
row3["cross_flag"] = 1
arr = [row1, row2]
print(arr)
arr.append(row3)
print(arr)


print(getSegs(arr))

# from datetime import datetime,time
# import time as t
#
# date_start = datetime.strptime("20180301", '%Y%m%d')
# date_end = datetime.strptime("20180331", '%Y%m%d')
# print(date_start)
# ts = t.mktime(date_start.timetuple())
# print(int(ts))
# total_days = (date_end - date_start).days + 1
# for day_number in range(total_days):
#     current_date = (date_start + datetime.timedelta(days = day_number)).date()
#     print(current_date)


lon = '2965351'
n = 0
str = ''
for i in range(len(lon)).__reversed__():
    str = lon[i] + str
    n += 1
    if(n == 5):
        str = '.' + str

print(str)
str = str +";"
print(str.rstrip(';'))

