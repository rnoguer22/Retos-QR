# Retos-QR

[Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Retos-QR.git)

---

La información deshasheada es: 
flag{QR_puede_usarse_para_esconder_mensajes}

---

Hemos hecho uso de POO para resolver este ejercicio, con una estructura basada en un archivo main.py que ejecuta las instrucciones en el archivo lanzador.py. Con esta practica, leemos la informacion de un qr mediante la libreria pyzbar, la cual resulta ser un hash cifrado en base64, no una, sino muchas veces. Posteriormente, pasamos al algoritmo de descifrado de hash en base64, y aplicaoms el algoritmo hasta obtener un mensaje con sentido, que resulta ser la información deshasheada mencionada anteriormente
:)
