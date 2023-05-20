import socket, os, datetime

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # creo socket

dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = 'localhost'
if not puerto:
    puerto = '16013'
try:
    ss.bind((dir_socket, int(puerto)))
except:
    print("Error al asignar una dirección al servidor")

while True:  
    data, dirc = ss.recvfrom(1024)
    peticion = data.decode('utf8')
    pid = os.fork()
    if pid: # padre, proceso servidor. 
        continue
    else: # hijo, proceso que gestiona el hijo
        if peticion == "hora":
            print("El cliente" , dirc , "ha pedido la hora")
            tiempo = datetime.datetime.now().time()
            ss.sendto(str(tiempo).encode('utf8'),dirc)
        elif peticion == "fecha":
            print("El cliente" , dirc , "ha pedido la fecha")
            tiempo = datetime.datetime.now()
            ss.sendto(str(tiempo).encode('utf8'),dirc)
        else:
            print("El cliente" , dirc , "se ha equivocado")
            ss.sendto("Error".encode('utf8'),dirc)       
        ss.close()
        print("El cliente" , dirc , "ha cerrado conexión")
        exit()