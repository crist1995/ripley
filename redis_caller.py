import redis

r=redis.Redis()
def getter(ciudad):
 data=r.hgetall(ciudad)
 return data
