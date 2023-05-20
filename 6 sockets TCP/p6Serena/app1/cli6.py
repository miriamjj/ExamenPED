import socket

socket_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')


if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '5555'

socket_cli.connect((dir_serv, int(puerto_serv)))

path = input('Introduzca el nombre del fichero: ')

socket_cli.send(path.encode('utf8'))


full_msg = ''
datos = "Empieza"
while datos:
    datos = socket_cli.recv(1024)
    full_msg += datos.decode('latin-1')
print(full_msg)

socket_cli.close()