import socket, select, sys

socket_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')
nombre_cliente = input('Nombre de usuario: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '8888'

if not nombre_cliente:
    nombre_cliente = 'usr'

socket_cli.connect((dir_serv, int(puerto_serv)))

socket_cli.send(nombre_cliente.encode('utf8'))

rlist = [sys.stdin, socket_cli]

msj_recibido = socket_cli.recv(1024).decode('utf-8')
print(msj_recibido)
while True:
    
    ready_rlist = select.select(rlist, [], [])
    for s in ready_rlist:
        if s == socket_cli:
            data = s.recv(1024)
            if not data:
                break
            print(data.decode())
        #respuesta = socket_cli.recv(1024)
        #print(respuesta.decode('utf8'))
        else:
            mensaje = input('>> ')
            socket_cli.sendall(mensaje.encode('utf8'))

            



    
    
    
    
