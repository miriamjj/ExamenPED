import os, time, sys, datetime
nombre_fifo = '/tmp/cliservFIFO'

if not os.path.exists(nombre_fifo):
    os.mkfifo(nombre_fifo)

while True:
    fifo_escritura = open(nombre_fifo, 'w')
    fecha_hora = datetime.datetime.now()
    fecha_hora_str = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
    fifo_escritura.write(fecha_hora_str)
    fifo_escritura.close()
    time.sleep(1)
