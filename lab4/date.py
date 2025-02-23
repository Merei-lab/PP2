import datetime
import math
#1
a = datetime.datetime.now()
print(a-datetime.timedelta(days=5))


#2
b=datetime.datetime.now()
print("",b-datetime.timedelta(days=1),"\n",b,"\n",b+datetime.timedelta(days=1))


#3
c=datetime.datetime.now()
print(c.replace(microsecond=0))


#4
f=datetime.datetime.now()
second=f.second
f1=datetime.datetime(2025,2,10,12,45,30)
second2=f1.second
print(abs(second-second2))
