import socket

socket_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')
path = input('Path del fichero: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '5555'


socket_cli.sendto(path.encode('utf8'), (dir_serv, int(puerto_serv)))

full_msg = ''
datos = "Empieza"
while datos:
    datos, dir = socket_cli.recvfrom(1024)
    full_msg += datos.decode('latin-1')
print(full_msg)

socket_cli.close()

