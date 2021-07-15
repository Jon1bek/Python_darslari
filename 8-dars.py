mehmonlar = ['Jonibek','Temurbek','Javlonbek','O`tkirbek']
print(mehmonlar)
for k in mehmonlar:
    print("Salom",k)
    print("Xayr",k)
    print(f"Hurmatli {k} sizni ertaga 9:00 da Nikoh oqshomiga taklish qilamiz")
print("Hurmat bilan Jonibek"  )
sonlar = list(range(0,10))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2}")
    dostlar = []
    print("5 ta do`stingizni kiriting ")
    for n in range(5):
        dostlar.append(input(f"{n+1}-dostingizni ismini kiriting: "))
    print(dostlar)