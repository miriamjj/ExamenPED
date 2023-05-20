import os, time, sys, datetime

rd, wd = os.pipe()
r, w = os.fdopen(rd,'rb',0), os.fdopen(wd,'wb',0)

pid = os.fork()

if pid: #padre (cliente)
    w.close()

    while True:
        fecha_hora = r.readline()
        if not fecha_hora:
            break
        print(fecha_hora.decode('utf8'))
else:
    r.close()
    fecha_hora_actual = datetime.datetime.now()
    fecha_hora_actual_str = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    w.write(fecha_hora_actual_str.encode('utf8'))
    w.flush()
    w.close()
