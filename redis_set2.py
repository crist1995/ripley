import redis

def set():
 r=redis.Redis()
 santiago={"latitud": -33.447868,"longitud": -70.665854}
 ny={"latitud": 40.6643,"longitud": -73.9385}
 zurich={"latitud":  47.379780,"longitud": 8.539383}
 auckland={"latitud": -36.850427,"longitud": 174.762842}
 georgia={"latitud": 32.602257,"longitud": -83.305323}
 r.hmset("santiago",santiago) # Set location of stgo
 r.hmset("nueva-york",ny) # set location of MY
 r.hmset("zurich",zurich) # set location of Zurich
 r.hmset("auckland",auckland) #set location of auckland
 r.hmset("georgia",georgia) #ser location of Georgia
# print(r.hgetall("zurich"))
