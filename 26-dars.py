f = "talabalar.txt"
with open(f) as file:
    talabalar = file.readlines()
print(talabalar)
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)