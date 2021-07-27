import datetime as dt 
hozir = dt.datetime.now() 
bugun = dt.date.today()
print("Bugungi sana:",bugun)
print(hozir) #sana-vaqt
print(hozir.time())
print(hozir.hour)
print(hozir.minute)
print(hozir.second)

mustaqillik = dt.datetime(2021,9,1,00,00,00) 
farq = mustaqillik - hozir  
kun = farq.days
sekund = int(farq.seconds)
minut = int(sekund/60)
soat = int(minut/60)
print(f"Mustaqillikga {kun} kun, {soat} soat, {minut} minut, {sekund} qoldi")