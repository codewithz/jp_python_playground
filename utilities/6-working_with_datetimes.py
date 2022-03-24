from datetime import  datetime
import time
dt1=datetime(2022,3,24)
print(dt1)

dt2=datetime.now()
print(dt2)

dt3=datetime.strptime("2022/04/23","%Y/%m/%d")
print(dt3)

dt4=datetime.fromtimestamp(time.time())
print(dt4)

print("DT1",dt1)
print("Formatted DT1",dt1.strftime("%Y/%m/%d"))