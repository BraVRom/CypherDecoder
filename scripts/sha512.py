import hashlib

def dcrypt_sha512(texto, passwords_list):
    for password in passwords_list:
        if hashlib.sha512(password.encode()).hexdigest() == texto:
            return f'Contraseña encontrada!\nPasswordSha512: {texto} | Password: {password}'
    return 'Contraseña no encontrada :('

def main():
    with open('rockyou.txt', 'r', errors='ignore') as archivo:
        passwords_list = [linea.strip() for linea in archivo]

    input_text = input("Introduce el texto cifrado en SHA-512:\n")
    result = dcrypt_sha512(input_text, passwords_list)
    print(result)

    input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()

