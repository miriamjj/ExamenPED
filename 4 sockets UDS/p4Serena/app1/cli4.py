import socket

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0) # creamos un socket: socket(dominio, tipo, protocolo)

nombre_socket = input('Introduzca el nombre del socket: ')

if not nombre_socket:
    nombre_socket = 'socket4'

socket_file = "/tmp/" + nombre_socket
s.connect(socket_file) # abrimos la conexión con el servidor

path = input('Introduzca el nombre del archivo: ')

s.send(path.encode('utf8'))

full_msg = ''
while True:
    mensaje = s.recv(1024)
    if not mensaje:
        break
    full_msg += mensaje.decode('latin-1')
print(full_msg)

s.close()