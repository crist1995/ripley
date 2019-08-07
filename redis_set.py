import redis

def set():
 r=redis.Redis()
 r.mset({"santiago latitud": -33.447868,"santiago longitud": -70.665854}) # Set location of stgo
 r.mset({"nueva-york latitud": 40.6643,"nueva-york longitud": -73.9385}) # set location of MY
 r.mset({"zurich latitud":  47.379780,"zurich longitud": 8.539383}) # set location of Zurich
 r.mset({"auckland latitud": -36.850427,"auckland longitud": 174.762842}) #set location of auckland
 r.mset({"georgia latitud": 32.602257,"georgia longitud": -83.305323}) #ser location of Georgia
