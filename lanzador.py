from QR.decode_base64 import Base64
from QR.decodeQR import DecodeQR

class Lanzador:

    def lanzar(self):
        qr = DecodeQR()
        encoded_hash = qr.decode_qr('flag.png')
        base_64 = Base64()
        for i in range(12):
            if i == 11:
                print('\nLa informacion del hash es: ', encoded_hash, '\n')
            encoded_hash = base_64.decode_hash(encoded_hash)
            base_64.write_hash(encoded_hash, 'hash.txt')