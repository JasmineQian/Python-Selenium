from time import strftime, localtime
import time
print(time.time())
time1=strftime('%Y-%m-%d %H:%M:%S', localtime())
time2 = strftime('%Y%m%d%H%M%S', localtime())
time3 = strftime('%y%m%d%H%M%S', localtime())
time4 = strftime('%Z %X %y%m%d%H%M%S', localtime())
time5 = strftime('"%a %b %d %H:%M:%S %Y', localtime())
print(localtime())
print(time1)
print(time2)
print(time3)
print(time4)
print(time5)

'''
1537942227.6411319
time.struct_time(tm_year=2018, tm_mon=9, tm_mday=26, tm_hour=14, tm_min=10, tm_sec=27, tm_wday=2, tm_yday=269, tm_isdst=0)
2018-09-26 14:10:27
20180926141027
180926141027
China Standard Time 14:10:27 180926141027
"Wed Sep 26 14:10:27 2018
'''


"""
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称%% %号本身  

"""