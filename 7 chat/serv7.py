import socket, os, select

lista_usuarios = []
lista_clientes = []

socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '8888'

socket_serv.bind((dir_serv, int(puerto_serv)))

socket_serv.listen(1)

def interaccion_cliente(nuevo_socket, usuario):
    while True:
        try:
            mensaje = nuevo_socket.recv(1024).decode()
            for cliente in lista_clientes:
                if cliente != nuevo_socket:
                    cliente.send(f'{usuario}: {mensaje}'.encode('utf8'))
                    #nuevo_socket.send(f'{usuario}: {mensaje}'.encode('utf8'))

        except Exception as e:
            pass
            #print(f'ERROR: {str(e)}')

while True:
    ns, direccion = socket_serv.accept()
    print(f'Conexión entrante desde {direccion[0]}:{direccion[1]}')

    lista_clientes.append(ns)

    usuario = ns.recv(1024).decode()
    lista_usuarios.append(usuario)

    pid = os.fork() #creamos proceso hijo para manejar la conexión con el nuevo cliente

    if pid == 0: # hijo
        socket_serv.close()
        ns.send('Bienvenido al chat'.encode('utf8'))
        interaccion_cliente(ns, usuario)



