from time import strftime, localtime
import time

print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
localtime()
time2 = strftime('%Y%m%d%H%M%S', localtime())
print(time2)
print(time.time())
