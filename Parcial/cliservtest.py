import unittest
from cliserv import Cliserv
# 1 pedir hora o fecha
# 2 comprueba lo que pides
# 3 devuelve lo que pide en un formato

class cliservTest(unittest.TestCase):
    def test_pide(self):
        devuelve = Cliserv()
        pide = devuelve.pide()
        self.assertIsInstance(pide,str)

    # Comprueba lo que pides
    def test_compr_hora(self):
        devuelve = Cliserv()
        hora = "hora"
        valido = devuelve.comprobar_hora(hora)
        self.assertTrue(valido)
    
    def test_compr_fecha_(self):
        devuelve = Cliserv()
        fecha = "fecha"
        valido = devuelve.comprobar_fecha(fecha)
        self.assertTrue(valido)

    def test_fecha_correcta(self):
        devuelve = Cliserv()
        fecha_str = "18/05/2023"
        fecha = devuelve.fecha()
        self.assertEquals(fecha_str, fecha)
    
    def test_hora_correcta(self):
        devuelve = Cliserv()
        hora_str = "20:30"
        hora = devuelve.hora()
        self.assertEquals(hora_str, hora)
    
    def test_error(self):
        devuelve = Cliserv()
        valido = devuelve.comprobar_hora("") and devuelve.comprobar_fecha("aoefj")
        self.assertFalse(valido)

	
		

	
	
	
		
	
if __name__ == '__main__':
    unittest.main()