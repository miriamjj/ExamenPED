import unittest, pytest
from cliserv import Cliserv

class cliservtest(unittest.TestCase):

    # Comprueba que se introduce lo que pide
    def test_pide(self):
        devuelve = Cliserv()
        pide = devuelve.pide()
        self.assertIsInstance(pide,str)

    # Comprueba que la palabra introducida es un palíndormo
    def test_palindromo(self):
        devuelve = Cliserv()
        cadena = "asa".encode("utf8")
        valido = devuelve.esPalindromo(cadena)
        self.assertTrue(valido)

    # Comprueba que la palabra no es un palíndromo
    def test_nopalindromo(self):
        devuelve = Cliserv()
        cadena = "numero".encode("utf8")
        valido = devuelve.esPalindromo(cadena)
        self.assertFalse(valido)

    # Comprueba que la palabra es parcial
    def test_parcial(self):
        devuelve = Cliserv()
        cadena = "a plan".encode("utf8")
        valido = devuelve.esParcial(cadena)
        self.assertTrue(valido)

    #Comprueba que el número es capicua
    def test_capicua(self):
        #devuelve = Cliserv()
        #cadena = "2002"
        #valido = devuelve.esCapicua(cadena)
        self.assertTrue(devuelve.esCapicua("2002"))

    #Comprueba que el número no es capicua
    def test_nocapicua(self):
        devuelve = Cliserv()
        cadena = "428".encode("utf8")
        valido = devuelve.esCapicua(cadena)
        self.assertFalse(valido)

    #Comprueba que no es un número natural
    def test_nonatural(self):
        devuelve = Cliserv()
        cadena = "hola".encode("utf8")
        valido = devuelve.esNatural(cadena)
        self.assertFalse(valido)

    #Comprueba que es un número natural
    def test_natural(self):
        devuelve = Cliserv()
        cadena = "1234".encode("utf8")
        valido = devuelve.esNatural(cadena)
        self.assertTrue(valido)


if __name__ == '__main__':
    unittest.main()




