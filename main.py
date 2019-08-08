import redis_caller as rc
import temp_time as tat
import redis_set2 as rs
import main2
import datetime as dt
import json

rs.set()
data=[]
hora=[]
ciudades=["santiago","nueva-york","zurich","auckland", "georgia"]
ajuste_horario=[-14400,-14400,7200,43200,-14400]
datos={}
for i in ciudades:
 datos[i]=[]
def cycle():
 for i in ciudades:
  data=main2.conn(i)
 for i in data[0]:
  time=dt.datetime.utcfromtimestamp(i+ajuste_horario[data[0].index(i)]).strftime("%Y/%m/%d %H:%M")
  hora.append(time)
 temp=data[1]
 for i in ciudades:
  datos[i]=[hora[ciudades.index(i)],temp[ciudades.index(i)]]
 for i in range(len(temp)):
  print(ciudades[i],temp[i])
# return ciudades,hora,temp #,datos
 return datos
