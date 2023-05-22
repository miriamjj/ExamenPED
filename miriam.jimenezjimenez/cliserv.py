
class Cliserv():

    def pide(self):
        peticion = input("Introduzca una palabra o un numero natural: ")
        return peticion

    def esNatural(self, peticion):
        try:
            peticion = int(peticion)
            if peticion >= 0:
                return True
            else:
                return False
        except ValueError:
            return False    

    def esPalindromo(self, peticion):
        peticion = peticion.lower()  # Convertir la palabra a minúsculas
        peticion = peticion.replace(" ", "")  # Eliminar espacios en blanco
        # Verificar si la palabra es igual a su reverso
        if peticion == peticion[::-1]:
            return True
        else:
            return False

    def esParcial(self):
        pass

    def esCapicua(self, peticion):
        peticion = str(peticion)
        return peticion == peticion[::-1]
        
    def resultado(self, peticion):
        if esNatural(peticion): # comprueba si lo introducido es un numero natural
            if esCapicua(peticion): #comprueba si el nº es capicua
                print("SI es capicua")
            else:
                print("NO es capicua")
        else: # si no es un numero natural
            if esPalindromo(peticion): # comprueba si es un palindromo
                print(f"{peticion} SI es un palíndromo.")
                #break
            else:
                print(f"{peticion} NO es un palíndromo.")
                #break
            print("NO NATURAL")







