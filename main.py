import time

from pythonping import ping

iord = input("请输入你想ping的ip或者域名") #iord全名是ip or domain(ip或者域名)

T1 = time.time()
ping(iord, count=1) #在1后面加上,verbose=True以查看实际延迟

T2 = time.time()
print('%dms' % ((T2 - T1) * 1000 - 14)) #这里请根据电脑响应速度更改
