import os, sys, time

# Creamos dos tuberías para que el cliente y els ervidor puedan comunicarse
rd1,wd1 = os.pipe() 
rd2,wd2 = os.pipe() 

# Creamos los descriptores para ambas tuberías
r1, w1 = os.fdopen(rd1,'rb',0), os.fdopen(wd1,'wb',0)
r2, w2 = os.fdopen(rd2,'rb',0), os.fdopen(wd2,'wb',0)

# Creamos el proceso hijo (servidor)
pid = os.fork()

if pid: # padre (cliente)
    r1.close()
    w2.close()
    
    #Escribimos el path completo del fichero en la tubería
    path = input("Insertar path: ")
    #"C:/Users/seren/fichero.txt" 
    #/mnt/c/Users/seren/fichero.txt
    w1.write(path.encode('utf8'))
    w1.flush()
    
    print("el cliente escribe el path para enviárselo al servidor")
    time.sleep(1)

    w1.close()
    # Leemos el mensaje que nos envía el servidor por la segunda tubería
    while True:
        mensaje = r2.readline()
        if not mensaje:
            break
        print(mensaje.decode('utf8').strip())

    r2.close()
    
else: # hijo (servidor)
    w1.close()
    r2.close()
    while True:
        pathFichero = r1.readline() # Leemos el path que nos envía el padre (cliente)
        if not pathFichero:
            break
        print("Hijo (servidor) ha recibido el path: " + pathFichero.decode('utf8'))
        
        ruta = pathFichero.decode()

        try:
            #Abrimos el archivo y leemos su contenido
            archivo = open(ruta, 'r')
            contenido = archivo.read()
            mensaje = contenido.encode('utf8')
        except Exception as e:
            # Si hay algún error, lo capturamos y lo enviamos al cliente
            mensaje = str(e).encode('utf8')

        # El hijo (servidor) escribe un mensaje en la segunda tubería
        w2.write(mensaje)
        w2.flush()
        time.sleep(1)

    r1.close()
    w2.close()
