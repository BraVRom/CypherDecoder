def descifrar_ascii(codigo_ascii):
    texto = ''
    for numero in codigo_ascii.split():
        texto += chr(int(numero))
    return texto

while True:
    codigo_ascii = input("Introduce el texto en código ASCII (EJEMPLO: 72 111 108 97 33): ")
    
    # Validar que la entrada contenga solo números
    if codigo_ascii.replace(" ", "").isdigit():
        resultado = descifrar_ascii(codigo_ascii)
        print("Texto descifrado:", resultado)
    else:
        print("Por favor, introduce solo números.")
        continue
    
    continuar = input("¿Deseas descifrar otro código ASCII? (Sí/No): ")
    if continuar.lower() not in ('si', 's', 'y'):
        break

