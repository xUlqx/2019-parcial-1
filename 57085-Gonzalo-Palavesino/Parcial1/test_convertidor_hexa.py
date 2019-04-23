import unittest
from interfaz_hexa import interfaz_hexa


class TestConvertidorHexa(unittest.TestCase):
  
    def test_convertidor_5(self):
        result = interfaz_hexa("5")
        self.assertEqual(result, "5")
    
    def test_convertidor_10(self):
        result = interfaz_hexa("10")
        self.assertEqual(result, "A")

    def test_convertidor_921(self):
        result = interfaz_hexa("921")
        self.assertEqual(result, "399")
    
    def test_convertidor_A(self):
        result = interfaz_hexa("A")
        self.assertEqual(result, "Error, el valor ingresado no es un numero")

    def test_convertidor_HolaMUndo(self):
        result = interfaz_hexa("Hola Mundo")
        self.assertEqual(result, "Error, el valor ingresado no es un numero")

    def test_convertidor_65535(self):
        result = interfaz_hexa("65535")
        self.assertEqual(result, "FFFF")


        

if __name__ == '__main__':
    unittest.main()