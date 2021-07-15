
narh = 0
non = True
salat = False
assorti = True
kompot = False
kabob = True

if kabob:
    print("Mijoz kabob oldi.")
    narh = narh + 20000;

if non:
    print("Mijoz non oldi.")
    narh = narh + 3000;

if assorti:
    print("Mijoz assorti oldi.")
    narh = narh + 5000;

if kompot:
    print("Mijoz kompot oldi.")
    narh = narh + 8000;
print(f"Jami narh {narh} so`m")

menu = ["osh","kabob","shashlik","tovuq"]
ovqat = input("Nima ovqat yeysiz? ")
if ovqat.lower() in menu:
    print("Buyurtma qilindi")
else:
    print("Afsuski bizda bunday ovqat yo`q")