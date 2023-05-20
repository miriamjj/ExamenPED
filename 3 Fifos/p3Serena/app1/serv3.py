import os, time, sys, datetime
fifo_cliente_servidor = '/tmp/cliservFIFOapp1'
fifo_servidor_cliente = '/tmp/servcliFIFOapp1'

if not os.path.exists(fifo_cliente_servidor):
    os.mkfifo(fifo_cliente_servidor)

if not os.path.exists(fifo_servidor_cliente):
    os.mkfifo(fifo_servidor_cliente)




while True:
    servidor_lee = open(fifo_cliente_servidor, 'r')
    path_fichero = servidor_lee.readline()
    print(path_fichero)
    servidor_lee.close()

    servidor_escribe = open(fifo_servidor_cliente, 'w')
    try:
        #Abrimos el archivo y leemos su contenido
        archivo = open(path_fichero, 'r')
        contenido = archivo.read()
        mensaje = contenido.encode('utf8')
    except Exception as e:
        # Si hay algún error, lo capturamos y lo enviamos al cliente
        mensaje = str(e).encode('utf8')

    servidor_escribe.write(contenido)
    servidor_escribe.close()


    