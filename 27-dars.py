faylnomi = 'new_file.txt'
ism = 'Jonibek O`ralov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')