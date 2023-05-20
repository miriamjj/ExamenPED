import socket, datetime

socket_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '5555'

socket_serv.bind( (dir_serv, int(puerto_serv)) )

print('El servidor está listo para recibir')

while True:
    datos, dirCliente = socket_serv.recvfrom(1024)
    print(datos.decode())
    fecha_hora = datetime.datetime.now()
    fecha_hora_str = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
    socket_serv.sendto(fecha_hora_str.encode('utf8'), dirCliente)
