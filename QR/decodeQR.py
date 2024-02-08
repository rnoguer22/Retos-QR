from pyzbar.pyzbar import decode
from PIL import Image

class DecodeQR:

    def decode_qr(self, image):
        image = Image.open(image)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            print("Tipo:", obj.type)
            print("\nDatos:", obj.data.decode("utf-8"))
            return obj.data.decode("utf-8")