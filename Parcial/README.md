En este directorio debe entregar los ficheros que conforman la respuesta al ejercicio.
# Sobre el proyecto 
Esta aplicación consiste en realizar un sencillo sistema cliente-servidor utilizando sockets UDP de Internet.

# Punto de escucha
El servidor escucha por un puerto UDP de Internet nº 16013

# Procedimiento:
1. El cliente se conecta al servidor mediante un socket UDP de Internet.
2. El servidor responderá con una cadena de carácteres que represente la fecha y la hora.
3. El cliente muestra la respuesta recibida por el servidor en su salida estándar.

# Aplicación: cliente-servidor de fecha y hora
Se desea realizar un sistema cliente-servidor con las siguientes características: 
1. El servidor atenderá peticiones en un Puerto UDP número 16013.
2. El servidor responderá a los mensajes enviados desde el cliente con:
	- Fecha actual del sistema
	- Hora actual del sistema
	- Error en otra situación

# Herramientas 
- Para ejecutar esta aplicación se necesita contar con un sistema operativo Unix
- La aplicación está creada en Python, se necesita contar la instalación de este lenguaje para ejecutarla. 

# Cómo ejecutar la Aplicación
Para ejecutar el servidor usa el siguiente comando:

    python3 Servidor.py

Para ejecutar el cliente usa el siguiente comando:

    python3 Cliente.py

Para ejecutar los Tests usa el siguiente comando:

	pytest cliserv.py


