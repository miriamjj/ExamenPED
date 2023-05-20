import socket, os

socket_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')


if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '5555'

socket_serv.bind((dir_serv, int(puerto_serv)))

while True:
    path, dirCliente = socket_serv.recvfrom(1024)
    print(path.decode())
    print(dirCliente)

    try:
        #Abrimos el archivo y leemos su contenido
        archivo = open(path, 'rb')
        mensaje = "Empieza"
        while mensaje:
            mensaje = archivo.read(1024)
            if isinstance(mensaje, str):
                contenido = mensaje.encode('utf8')
            elif isinstance(mensaje, bytes):
                contenido = mensaje
            socket_serv.sendto(contenido, dirCliente)
        
    except Exception as e:
        contenido = str(e).encode('utf8')



    

