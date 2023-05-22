import socket, os, sys, time
from cliserv import Cliserv

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # creo socket UDP

dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = 'localhost'
if not puerto:
    puerto = '16013'
try:
    ss.bind((dir_socket, int(puerto)))
except:
    print("Error al asignar una dirección al servidor")

devuelve = Cliserv()
while True:  
    data, dirc = ss.recvfrom(1024)
    peticion = data.decode('utf8')
    pid = os.fork()
    if pid: # padre, proceso servidor. 
        continue
    else: # hijo, proceso que gestiona el hijo
        if devuelve.esNatural(peticion): #comprueba si es un nº natural
            print("El cliente" , dirc , "ha introducido un numero")
            #ss.sendto("SI palindromo".encode('utf8'),dirc)
            if devuelve.esCapicua(peticion): # comprueba si el nº es capicua
                ss.sendto("SI capicua".encode('utf8'),dirc)
            else: #si no capicua
                ss.sendto("NO capicua".encode('utf8'),dirc)
        else: # si no nº natural
            # ss.sendto("NO NATURAL".encode('utf8'),dirc)
            if devuelve.esPalindromo(peticion): #comrpueba si palindromo
                ss.sendto("SI palindromo".encode('utf8'),dirc)
            else: # si no palindromo
                ss.sendto("NO palindromo".encode('utf8'),dirc)       
        ss.close()
        print("El cliente" , dirc , "ha cerrado conexión")
        exit()
