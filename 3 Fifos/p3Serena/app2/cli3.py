import os, time, sys
nombre_fifo = '/tmp/cliservFIFO'

if not os.path.exists(nombre_fifo):
    print("El servidor no está disponible.")
    exit()

fifo_lectura = open(nombre_fifo, 'r')
dato = fifo_lectura.readline()
print(dato)
fifo_lectura.close()
    
