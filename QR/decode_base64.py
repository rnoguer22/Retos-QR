import base64

class Base64:

    def __init__(self, encoded_hash):
        self.encoded_hash = encoded_hash
        

    def decode_base64_hash(self, hash):
        try:
            # Decodifica el hash en Base64
            decoded_hash = base64.b64decode(hash)
            return decoded_hash.decode('utf-8')
        except Exception as e:
            return f"Error: {str(e)}"


    def decode_long_hash(self):
        split_hash = ''
        correct_hash = []
        for i in range(len(self.encoded_hash)):
            split_hash += self.encoded_hash[0]
            self.encoded_hash = self.encoded_hash[1:]
            try:
                hash_bueno = base64.b64decode(split_hash)
                correct_hash.append(hash_bueno.decode('utf-8'))
                split_hash = ''
            except Exception as e:
                print(f"Error: {str(e)}")
        return correct_hash
    


if __name__ == "__main__":
    encoded_hash = "Vm0wd2QyUXlWa2hWV0doVllteEtWMVl3WkRSWFJteFZVbTVrVmxKc2NIcFhhMk0xVmpGS2RHVkdXbFpOYm1oUVdWZDRTMk14VG5OWGJHUlRUVEZLVVZkV1kzaFRNVWw0V2toR1VtSlZXbFJXYWtwdlpWWmFkR05GU214U2JWSkpWbTEwYzJGV1NuUlZiR2hoVmpOb2FGWldXbUZqYkhCSlkwZDRVMkpXU2xsV1Z6QXhVekpHUjFOdVVtaFNlbXhXVm0weGIxSkdjRmRYYlhSWFRWWndlbFl5TVRSVk1rcFhVMnhzVjFaNlFYaFdSRXBIVWpGT2RWUnNhR2hsYlhoWlYxZDRiMVV3TUhoV1dHaFlZbGhTV0ZSV2FFTlRiR3QzV2tSU1ZrMUVSa1pXYlhCaFZqQXhkVlZ1V2xaaGExcGhXbFphVDJOdFNrZFRiV3hvWld4YWIxWnRNVEJXYXpGWFUydGtXRmRIYUZsWmEyaERZekZhYzFWclpGUmlSM2hYVmpKNGExWlhTa2RqUmxwWFlsaFNlbFpxUm1GU2JVVjZZVVprYUdFelFrbFdiWEJIVkRKU1YxZHVUbFJpVjNoVVZGY3hiMkl4V25STlJFWnJUVlZ3ZVZSV1ZtdGhiRXAwWVVoT1ZtRnJOVlJXTVZwaFkxWkdWVkpzVGs1WFJVcElWbXBLTkdFeFdsaFRiRnBxVWxkU1lWbFhjekZqYkZweFVtMUdVMkpWVmpaWlZWcHJWakZLVjJOSE9WaGhNVnBvVmtSS1RtVldUbkpoUjJoVFlrVndWVlp0TURGUk1rbDRWMWhvV0dKRk5WUlVWbFY0VGxaYWRFNVZPVmRpVlhCSVdUQmFjMWR0U2toaFJsSmFUVlp3VkZacVJuZFNWbEp5VGxkc1UySkhPVE5XYTFwaFZURlZlVkpyWkZoaWEzQndWV3RhZDFsV1duTlhibVJPVFZac00xWXlNVWRWTWtwR1RsUkdWazF1YUZoWlZWVjRZekZPY21KR2FGZFNXRUV5VjJ4V1lWbFdXWGhqUld4VllrWktjRlZxUmt0V1ZscEhWV3RLYTAxRVJsTlZSbEYzVUZFOVBRPT0="
    base_64 = Base64(encoded_hash)
    print(base_64.decode_long_hash())