class Talaba:
    def __init__(self,ism,familiya,t_yil):
        self.ism = ism
        self.familiya = familiya
        self.t_til = t_yil
        self.kursi = 1
    def tanishtir(self):
        return(f"Ismim {self.ism} familiyam {self.familiya} tug`ilgan yilim {self.t_yil}")
talaba1 = Talaba("Jonibek","O`ralov",2001)
talaba2 = Talaba("Temurbek","O`ralboyev",2001)
print(talaba1.kursi())
 