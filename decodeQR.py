from pyzbar.pyzbar import decode
from PIL import Image

# Carga la imagen que contiene el código QR
image = Image.open("flag.png")

# Decodifica el código QR
decoded_objects = decode(image)

# Imprime la información decodificada
for obj in decoded_objects:
    print("Tipo:", obj.type)
    print("Datos:", obj.data.decode("utf-8"))
