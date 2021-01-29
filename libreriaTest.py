import unittest
import libreria as cpl

class TestLibreria(unittest.TestCase):

    def test_suma(self):
        c1=(-6,-9)
        c2=(-5,8)
        self.assertEqual(cpl.suma(c1,c2),(-11,-1))

    def test_resta(self):
        c1=(-6,-9)
        c2=(-5,8)
        self.assertEqual(cpl.resta(c1,c2),(-1,-17))

    def test_producto(self):
        c1=(-6,-9)
        c2=(-5,8)
        self.assertEqual(cpl.producto(c1,c2),(102,-3))

    def test_division(self):
        c1=(-6,-9)
        c2=(-5,8)
        self.assertEqual(cpl.division(c1,c2),(-42/89,93/89))

    def test_conjugado(self):
        c1=(-6,-9)
        self.assertEqual(cpl.conjugado(c1),(-6,9))

    def test_modulo(self):
        c2=(3,4)
        self.assertEqual(cpl.modulo(c2),(5))

    def test_polarCartesiano(self):
        c1=(2 ** (1 / 2), 45)
        self.assertEqual(cpl.polarCartesiano(c1),(1,1))

    def test_fase(self):
        c1=(6,15)
        self.assertEqual(cpl.fase(c1), 68.19859051364818)

    def test_cartesianoPolar(self):
        c1=(1,1)
        self.assertEqual(cpl.cartesianoPolar(c1), (round(2 ** (1 / 2),2), 45))
    
    
    
if __name__=='__main__':
    unittest.main()
