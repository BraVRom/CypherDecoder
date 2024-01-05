import hashlib
import os

# Solicita al usuario que ingrese el hash MD5.
hash_md5_input = input("Introduce el texto hasheado en md5:\n")
print()  # Agregamos una línea en blanco

# Obtiene la ruta completa del archivo 'rockyou.txt' en el directorio 'scripts/'.
rockyou_path = os.path.join('scripts', 'rockyou.txt')

# Verifica si el archivo 'rockyou.txt' existe en la ruta especificada.
if os.path.exists(rockyou_path):
    with open(rockyou_path, 'r', errors='ignore') as archivo:
        passwordsList = [linea.strip() for linea in archivo]
else:
    print("El archivo 'rockyou.txt' no se encuentra en la ruta 'scripts/'. Asegúrate de que el archivo exista en esa ubicación.")

# Función para calcular el hash MD5 de una cadena.
def hash_md5(cadena):
    resultado = hashlib.md5(cadena.encode())
    return resultado.hexdigest()

# Función para descifrar el hash MD5 proporcionado.
def decipherMd5(passwordMd5):
    for password in passwordsList:
        if hash_md5(password) == passwordMd5:
            return("Encontrada 〈 ͡° ͜ʖ ͡°)   \npasswordMd5: " + str(passwordMd5) + " | Password: " + str(password))
    return "Contraseña no encontrada _(._.)_"

# Llama a la función con el hash MD5 proporcionado por el usuario y muestra el resultado.
print(decipherMd5(hash_md5_input))

