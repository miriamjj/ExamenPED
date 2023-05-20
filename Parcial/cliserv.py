import datetime

class Cliserv():
    
    def pide(self):
        peticion = input("Introduzca si quiere saber la fecha o la hora: ")
        return peticion
   
    def comprobar_fecha(self, peticion):
        if peticion == "fecha":
            return True
        else:
            return False
        
    def comprobar_hora(self, peticion):
            if peticion == "hora":
                 return True
            else:
                 return False
    
    def fecha(self):
        return datetime.datetime.now()
    
    def hora(self):
        return datetime.datetime.now().time()
