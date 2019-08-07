import redis_caller as rc
import temp_time as tat
import redis_set2 as rs
import main2
rs.set()
ciudad=["santiago","zurich"]
ciudades=["santiago","nueva-york","zurich","auckland", "georgia"]
for i in ciudades:
 print(i)
 main2.conn(i)
# pos= rc.getter(i)
# print(pos[b'longitud'])
# print(tat.gettat(pos[0],pos[1]))
# print(i)
