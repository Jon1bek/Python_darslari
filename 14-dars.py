trackers=[]
for n in range(10):
    new_car = {
        "model" : "tracker",
        "rang"  : None,
        "yil" : 2021,
        "narx" : None,
        "yurgan" : 0,
        "uzatish qutisi" : "avtomat"    
    }
    trackers.append(new_car)
print(trackers)
for trac in trackers[:3]:
    trac["rang"] = "qizil" 
for trac in trackers:
    print(trac)
