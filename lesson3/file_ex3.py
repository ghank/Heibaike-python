#/usr/bin/env python
# coding: utf-8


# import codecs
# import re
# f = codecs.open('beijing_jt.csv', 'r', 'utf-8')
# test_list = f.readlines()
# f.close()
#
# str = ''.join(test_list[1:40])
# jt_info = str.split(',')
# jt_stations = jt_info[-1].split('\r\n \r\n')
# # print jt_stations[1]
#
# print jt_info[1]
# station_pattern = (r'(?P<number>[0-9]+)\s(?P<name>\D+)')
# station_list = []
# stations = re.findall(station_pattern, jt_info[-1])
# for tmp in stations:
#     # print tmp[0], tmp[1].strip()
#     station_list.append(tmp[1].strip())
#
# for tmp in jt_stations:
#     stations = re.search(station_pattern,tmp.strip())
#     print stations.group('number'),stations.group('name')
#
# result = {}
# result[jt_info[1]] = station_list
# print result

# station_list_reverse = station_list.reverse()
# print station_list_reverse



# import csv
#
# with open('beijing_jt.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         beijing_jt_dict = dict(zip(row['linenum'], row['station']))
#         print row['station']
#
# print beijing_jt_dict.values()

import csv
import re

csvfile = open(r'beijing_jt.csv', 'r')
reader = csv.reader(csvfile)
next(reader)

result={}

while True:
    try:
        jt_info = next(reader)
    except:
        break

    station_pattern = (r'(?P<number>[0-9]+)\s(?P<name>\D+)')
    station_list = []
    stations = re.findall(station_pattern, jt_info[-1].decode('utf-8'))
    for tmp in stations:
        # print tmp[0], tmp[1].strip()
        station_list.append(tmp[1].strip())

    result[jt_info[1]] = station_list

csvfile.close()

while True:
    find_station = raw_input(u"请输入你想查询的公交站名：")
    print find_station

    for k, v in result.iteritems():
        if unicode(find_station, 'utf-8') in v:
            print k, find_station



