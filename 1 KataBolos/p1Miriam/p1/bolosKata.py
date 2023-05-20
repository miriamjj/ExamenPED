
class Partida():


    def marcador_valido(self, marcador):
        if len(marcador)>11 or len(marcador)<10:
            return False
        if len(marcador)==11 and marcador[-2][0] + marcador[-2][1] != 10:
            return False 

        for ronda in marcador:
            if len(ronda) != 2:
                return False
            elif ronda[0]+ronda[1]>10:
                return False
            elif ronda[0]<0 or ronda[1]<0:
                return False
            else:
                return True
   
    def hay_strike(self, ronda):
        if ronda == (10,0):
            return True
        return False 
    
    def hay_spare(self, ronda):
        if ronda[0] + ronda[1] == 10 and ronda[0]!=10:
            return True
        return False
    
    def puntuacion(self, marcador):
        suma_puntuaciones = 0
        strike = 0
        spare = False
        if self.marcador_valido(marcador):    
            for i,ronda in enumerate(marcador):
                if self.hay_strike(ronda) and i != 10:
                    strike = strike + 1
                    if spare:
                        suma_puntuaciones +=10
                        spare = False
                    continue
                
                if strike == 1:
                    suma_puntuaciones = suma_puntuaciones + 10 + 2*ronda[0] + 2*ronda[1]
                    strike = 0
                elif strike > 1:
                    suma_puntuaciones = suma_puntuaciones + (strike-1)*3*10 + 3*ronda[0] + 2*ronda[1]
                    strike = 0
                elif spare:
                    suma_puntuaciones = suma_puntuaciones + 2*ronda[0] + ronda[1]
                    spare = False
                else:
                    suma_puntuaciones = suma_puntuaciones + ronda[0] + ronda[1]
                
                if self.hay_spare(ronda):
                    spare = True

            return suma_puntuaciones
        return None

        
