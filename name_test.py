import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('jonibek','Uralov')  
        self.assertEqual(formatted_name, 'Jonibek Uralov')
    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(name,'Hasan Olimovich Husanov')

unittest.main()