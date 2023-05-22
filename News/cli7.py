import socket, sys, errno, os

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '8888'

mi_usuario = input('Nick: ')

socket_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cli.connect((dir_serv, int(puerto_serv)))
socket_cli.setblocking(False)

# Opcional solo en caso de que quieras que aparezca el nick en el log del servidor
#usuario = mi_usuario.encode('utf-8') 
#socket_cli.send(usuario)
#if recibido == 'ERROR Ese usuario ya está en uso, prueba con otro nombre.':
#    print(recibido)
#    sys.exit()

N = input("Introduzca el numero de días: ")
socket_cli.send(n.encode('utf-8'))
while True:
    data = s.recv(1024) # Cliente lee contenido del socket
    if not data: # Sale del bucle si ha llegado a un end of file (EOF)
        break
    print(data.decode('utf8').strip())



pid=os.fork()
if pid:
    while True:
        titulo = input('Titulo: ')
        socket_cli.send(titulo.encode('utf8'))
        socket_cli.send(mi_usuario.encode('utf8'))
        print('Escribe articulo y linea vacia para terminar.')
        while True:
            mensaje = input()
            if not mensaje:
                socket_cli.send(mensaje.encode('utf8'))
                print('Articulo enviado')
                break
            socket_cli.send(mensaje.encode('utf8'))

else:
    while True:
        try:
            while True:
                data = s.recv(1024) # Cliente lee contenido del socket
                if not data: # Sale del bucle si ha llegado a un end of file (EOF)
                    break
                print(data.decode('utf8').strip())

        except IOError as e:
            if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
                print('reading error', str(e))
                sys.exit()
            continue

        except Exception as e:
            print('GENERAL ERROR', str(e))
            sys.exit()
