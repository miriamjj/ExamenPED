import unittest 
from bolosKata import Partida

class bolosTest(unittest.TestCase):

    # Comprueba que en una ronda no puede haber solo una tirada de bolos
    def test_ronda_no_valida(self):
        partida = Partida()
        marcador = [(9, ),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        valido = partida.marcador_valido(marcador)
        self.assertFalse(valido)

    # Compueba que en una ronda no puede haber más de dos tiradas de bolos
    def test_ronda_no_valida2(self):
        partida = Partida()
        marcador = [(9,2,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        valido = partida.marcador_valido(marcador)
        self.assertFalse(valido)

    # Comprueba que en una ronda no puede haber más de 10 bolos tirados
    def test_ronda_mas_bolos(self):
        partida = Partida()
        marcador = [(9,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        valido = partida.marcador_valido(marcador)
        self.assertFalse(valido)
    
    # Comprueba que en una ronda no puede haber ninguna tirada negativa
    def test_ronda_bolos_negativos(self):
        partida = Partida()
        marcador = [(2,-1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        valido = partida.marcador_valido(marcador)
        self.assertFalse(valido)

    # Comprueba que no puede haber 11 rondas
    def test_ronda_bonus_no_valida(self):
        partida = Partida()
        marcador = [(5,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(4,3),(5,1)]
        valido = partida.marcador_valido(marcador)
        self.assertFalse(valido)
    
    # Comprueba que no puede haber más de 10 rondas
    def test_hay_mas_rondas(self):
        partida = Partida()
        marcador = [(4,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0), (2,3),(4,6),(5,2)]
        valido = partida.marcador_valido(marcador)
        self.assertFalse(valido)
    
    # Comprueba que no puede haber 9 rondas
    def test_hay_1ronda_menos(self):
        partida = Partida()
        marcador = [(9,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        valido = partida. marcador_valido(marcador)
        self.assertFalse(valido)
    
    # Comprueba que no puede haber menos de 10 rondas
    def test_hay_menos_rondas(self):
        partida = Partida()
        marcador = [(9,3),(0,0),(0,0)]
        valido = partida. marcador_valido(marcador)
        self.assertFalse(valido)

    # Partida todo 0 
    def test_partida_cero(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total, 0)

    # Comprueba que suma la tirada de un bolo 
    def test_partida_uno(self):
        partida = Partida()
        marcador = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total, 1)
    
    # Comprueba que suma bien las rondas con varios puntos
    def test_partida_varios_puntos(self):
        partida = Partida()
        marcador = [(4,2),(3,1),(2,5),(2,2),(9,0),(4,1),(3,0),(1,4),(6,2),(4,4)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total, 59)
    
    def test_partida_varios_puntos2(self):
        partida = Partida()
        marcador = [(1,3),(2,0),(0,6),(3,3),(2,3),(0,1),(1,1),(4,3),(3,1),(1,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total, 38)
    
    # Partida puntuaciones todo 1
    def test_partida_todo1(self):
        partida = Partida()
        marcador = [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total, 20)

    # Comprueba que suma bien la puntuación total cuando hay un strike en la primera ronda
    def test_partida_1strike(self):
        partida = Partida()
        marcador = [(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,20)

    # Comprueba que suma bien la puntuación total cuando hay un strike en cualquier ronda 
    def test_partida_otro_strike(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,20)

    # Comprueba que suma bien la puntuación total cuando hay dos strikes seguidos
    def test_partida_2strikes(self):
        partida = Partida()
        marcador = [(10,0),(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,44)

    # Comprueba que suma bien la puntuación total con 3 strikes seguidos
    def test_partida_3strikes(self):
        partida = Partida()
        marcador = [(10,0),(10,0),(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,74)

    # Comprueba que suma bien la puntuación total cuando hay varios strikes no seguidos
    def test_partida_strikes_no_consecutivos(self):
        partida = Partida()
        marcador = [(10,0),(4,1),(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,40)
    
    # Comprueba que suma bien la puntuación total en caso de haber un spare en la primera ronda
    def test_1spare(self):
        partida = Partida()
        marcador = [(5,5),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,19)

    # Comprueba que suma bien la puntuación total en caso de haber un spare en cualquier ronda
    def test_otro_spare(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(8,2),(6,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,25)

    # Comprueba que suma bien la puntuación total en caso de haber dos spare seguidos
    def test_2spare(self):
        partida = Partida()
        marcador = [(5,5),(9,1),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,38)

    # Comprueba que suma bien la puntuación total en caso de haber tres spare seguidos
    def test_3spare(self):
        partida = Partida()
        marcador = [(5,5),(9,1),(8,2),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,56)
    
    # Comprueba que suma bien la puntuación total en caso de haber un strike y un spare seguidos
    def test_strike_spare(self):
        partida = Partida()
        marcador = [(10,0),(9,1),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,39)

    # Comprueba que suma bien la puntuación total en caso de haber un spare y un strike seguidos
    def test_spare_strike(self):
        partida = Partida()
        marcador = [(9,1),(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,40)
    
    # Comprueba que suma bien la puntuación total en caso de haber un spare y dos strikes seguidos
    def test_spare_2strike(self):
        partida = Partida()
        marcador = [(9,1),(10,0),(10,0),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,64)

    def test_bonus_strike(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(10,0),(2,3)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,20)
    
    def test_bonus_spare(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(9,1),(2,3)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,17)
    
    def test_bonus_strike_spare(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(10,0),(9,1)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,30)
    
    def test_bonus_spare_strike(self):
        partida = Partida()
        marcador = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(9,1),(10,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,30)

    def test_todo_spare(self):
        partida = Partida()
        marcador = [(9,1),(9,1),(9,1),(9,1),(9,1),(9,1),(9,1),(9,1),(9,1),(9,1),(9,1)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,200)

    def test_todo_strike(self):
        partida = Partida()
        marcador = [(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0)]
        total = partida.puntuacion(marcador)
        self.assertEqual(total,300)
    

if __name__ == '__main__':
  unittest.main()