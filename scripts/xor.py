# Función para realizar la operación XOR en dos caracteres
def xor_decrypt(ciphertext, key):
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
        decrypted += decrypted_char
    return decrypted

# Pedir al usuario el texto cifrado y la clave
ciphertext = input("Introduce el texto cifrado en XOR: ")
key = input("Introduce la clave: ")

decrypted_text = xor_decrypt(ciphertext, key)

print("Texto descifrado:", decrypted_text)

input("Presiona Enter para salir...")

