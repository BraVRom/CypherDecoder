import hashlib

# Necesitas tener rockyou.txt en el mismo directorio que sha256.py
try:
    with open('rockyou.txt', 'r') as archivo:
        passwordsList = [linea.strip() for linea in archivo]
except FileNotFoundError:
    print("Error: No encuentro el rockyou.txt (╥﹏╥)")
    exit(1)
except Exception as e:
    print("Error al cargar el archivo de contraseñas:", e)
    exit(1)

def dcryptSha256(texto):
    for password in passwordsList:
        if hashlib.sha256(password.encode()).hexdigest() == texto:
            return 'Contraseña encontrada! <(^_^)>    \n    PasswordSha256: ' + str(texto) + " | " + "Password: " + str(password)
    return 'Contraseña no encontrada :('

while True:
    texto = input("Introduce el texto para calcular su valor SHA-256 (o presiona Enter para salir):\n")
    if not texto:
        break

    try:
        sha256_result = hashlib.sha256(texto.encode()).hexdigest()
    except Exception as e:
        print("Error al calcular el valor SHA-256:", e)
        continue

    resultado = dcryptSha256(sha256_result)
    print(f'Valor SHA-256 de "{texto}": {sha256_result}')
    print(resultado)
