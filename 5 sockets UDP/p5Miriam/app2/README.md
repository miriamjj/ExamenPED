# Sobre el proyecto 
Esta práctica consiste en realizar un sencillo sistema cliente-servidor utilizando sockets UDP de Internet.

# Aplicación: cliente-servidor de fecha y hora
El objetivo es realizar una sencilla aplicación cliente-servidor que muestre la fecha y hora. 
1. El cliente se conecta al servidor mediante un socket UDP de Internet.
2. El servidor responderá con una cadena de carácteres que represente la fecha y la hora.
3. El cliente muestra la respuesta recibida por el servidor en su salida estándar.

# Cómo ejecutar la Aplicación
Para ejecutar el servidor usa el siguiente comando:

    make servidor

Para ejecutar el cliente usa el siguiente comando:

    make cliente

Para limpiar una vez ejecutada la Aplicación:

    make clean
