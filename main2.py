import random
import temp_time as tat
import redis_set2
import redis_caller as rc
redis_set2.set()
counter=0
def conn(ciudad):
  try:
   value=random.random()
   pos=rc.getter(ciudad)
   if(value< 0.1):
#    print("hubo un problema con ",ciudad)
    raise Exception("La api ha fallado")
   else:
#    print(tat.gettat(pos[b'latitud'],pos[b'longitud']))
    print(pos[b'latitud'],pos[b'longitud'])
#    print("no ha habido problemas")
  except Exception as ex:
   conn(ciudad)
