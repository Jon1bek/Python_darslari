def oraliq(min,max,qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
print(oraliq(1,101,2))