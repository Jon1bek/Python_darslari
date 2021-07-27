#PICKLE FAYLGA YOZISH 
 
import pickle

talaba1 = {'ism':'Jonibek', 'familiy':'O`ralov', 'tyil':2001, 'kurs': 2}
talaba2 = {'ism':'Temurbek', 'familiya':'O`ralboyev', 'tyil':2006, 'kurs': 1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)