import socket
import os

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)  # creamos un socket

nombre_socket = input('Introduzca el nombre del socket: ')

if not nombre_socket:
    nombre_socket = 'socket4'

# Eliminamos el archivo de socket si existe
socket_file = "/tmp/" + nombre_socket
if os.path.exists(socket_file):
    os.remove(socket_file)


s.bind(socket_file) # asignamos una dirección al socket
s.listen(5)

while True:
    ns, direccion = s.accept()
    print('Nueva conexion establecida')

    peticion = ns.recv(1024) # hacer un bucle para que pueda leer cualquier tamaño
    print(peticion.decode('utf8'))

    try:
        #Abrimos el archivo y leemos su contenido
        with open(peticion, 'rb') as f:
            while True:
                datos = f.read(1024)
                if not datos:
                    break
                if isinstance(datos, str):
                    contenido = datos.encode('utf8')
                elif isinstance(datos, bytes):
                    contenido = datos
                ns.send(contenido)
    except Exception as e:
        contenido = str(e).encode('utf8')
        ns.send(contenido)


    ns.close()
