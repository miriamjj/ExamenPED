import os, time, sys, datetime
fifo_cliente_servidor = '/tmp/cliservFIFOapp1'
fifo_servidor_cliente = '/tmp/servcliFIFOapp1'

if not os.path.exists(fifo_cliente_servidor):
    os.mkfifo(fifo_cliente_servidor)

if not os.path.exists(fifo_servidor_cliente):
    os.mkfifo(fifo_servidor_cliente)

#while True:
cliente_escribe = open(fifo_cliente_servidor, 'w')
path = input()
cliente_escribe.write(path)
cliente_escribe.close()

cliente_lee = open(fifo_servidor_cliente, 'r')

contenido = cliente_lee.read()
print(contenido)

    
cliente_lee.close()