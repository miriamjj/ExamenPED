import socket, datetime, os

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

nombre_socket = input('Introduzca el nombre del socket: ')

if not nombre_socket:
    nombre_socket = 'socket4'

# Eliminamos el archivo de socket si existe
socket_file = "/tmp/" + nombre_socket
if os.path.exists(socket_file):
    os.remove(socket_file)

s.bind(socket_file)
s.listen(1)

while True:
    ns, dir = s.accept()
    print('Nueva conexion establecida')
    peticion = ns.recv(1024)
    print(peticion.decode())
    fecha_hora = datetime.datetime.now()
    fecha_hora_str = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
    ns.send(fecha_hora_str.encode('utf8'))
    ns.close()