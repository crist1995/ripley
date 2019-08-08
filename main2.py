import redis
import random
import temp_time as tat
import redis_caller as rc
counter=0
data=[]
data2=[]
def conn(ciudad):
  try:
   value=random.random()
   pos=rc.getter(ciudad)
   if(value< 0.1):
    print("hubo un problema con ",ciudad)
    raise Exception("La api ha fallado")
   else:
    print("no ha habido problemas")
    info=tat.gettat(pos[b'latitud'],pos[b'longitud'])
    data.append(info[0])
    data2.append(info[1])
  except Exception as ex:
   conn(ciudad)
  return data,data2
