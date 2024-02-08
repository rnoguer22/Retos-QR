import base64

class Base64:


    def decode_hash(self, encoded_hash):
        split_hash = ''
        correct_hash = ''
        for _ in range(len(encoded_hash)):
            split_hash += encoded_hash[0]
            encoded_hash = encoded_hash[1:]
            try:
                hash_bueno = base64.b64decode(split_hash)
                correct_hash += hash_bueno.decode('utf-8')
                split_hash = ''
            except Exception as e:
                pass
        return correct_hash


    def write_hash(self, hash, file):
        try:
            with open(file, 'a') as hash_file:
                hash_file.write(hash + '\n')
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")