import redis_caller as rc
import temp_time as tat
import redis_set2 as rs
import main2
import datetime as dt

rs.set()
data=[]
hora=[]
ciudades=["santiago","nueva-york","zurich","auckland", "georgia"]
ajuste_horario=[-14400,-14400,7200,43200,-14400]
def cycle():
 for i in ciudades:
  data=main2.conn(i)
 for i in data[0]:
  hora.append(dt.datetime.utcfromtimestamp(i+ajuste_horario[data[0].index(i)]).strftime("%Y/%m/%d %H:%M"))
 temp=data[1]
 return ciudades,hora,temp
