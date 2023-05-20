import socket

socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '5555'

socket_serv.bind((dir_serv, int(puerto_serv)))

socket_serv.listen(1)

while True:
    ns, dirCliente = socket_serv.accept()
    print('Conexión establecida')

    path_fichero = ns.recv(1024)

    try:
        #Abrimos el archivo y leemos su contenido
        archivo = open(path_fichero, 'rb')
        mensaje = "Empieza"
        while mensaje:
            mensaje = archivo.read(1024)
            if isinstance(mensaje, str):
                contenido = mensaje.encode('utf8')
            elif isinstance(mensaje, bytes):
                contenido = mensaje
            ns.send(contenido)
        
    except Exception as e:
        contenido = str(e).encode('utf8')

    ns.close()

