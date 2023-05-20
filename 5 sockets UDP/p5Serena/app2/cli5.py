import socket

socket_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 

#s.bind( (socket.INADDR_ANY, 9999) )

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '5555'

mensaje = '¿Qué hora es?'

socket_cli.sendto(mensaje.encode('utf8'), (dir_serv, int(puerto_serv)))

respuesta, dir = socket_cli.recvfrom(1024)
print(respuesta.decode())

socket_cli.close()
