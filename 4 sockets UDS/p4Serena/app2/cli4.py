import socket, os

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

nombre_socket = input('Introduzca el nombre del socket: ')

if not nombre_socket:
    nombre_socket = 'socket4'

socket_file = "/tmp/" + nombre_socket
s.connect(socket_file)

peticion = '¿Qué hora es?'
s.send(peticion.encode('utf8'))

respuesta = s.recv(1024)
print(respuesta.decode())

s.close()
