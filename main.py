import redis_caller as rc
import temp_time as tat
import redis_set2 as rs
import main2
rs.set()
data =[]
ciudad=["santiago","zurich"]
ciudades=["santiago","nueva-york","zurich","auckland", "georgia"]
def cycle():
 for i in ciudades:
#  print(i)
  main2.conn(i)
  pos= rc.getter(i)
#  print(pos[b'longitud'])
  data.append(tat.gettat(pos[b'latitud'],pos[b'longitud']))
 return data
