import socket, sys
from cliserv import Cliserv

# creo socket
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 

dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = 'localhost'
if not puerto:
    puerto = '16013'

devuelve = Cliserv()
peticion = devuelve.pide()
sc.sendto(peticion.encode('utf8'), (dir_socket, int(puerto)))

data, dir = sc.recvfrom(1024)
sys.stdout.write(data.decode('utf8').strip()) 
print("\n")
sc.close()
