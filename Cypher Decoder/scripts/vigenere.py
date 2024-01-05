from random import sample
from itertools import product as producto_cartesiano

def generador_claves(key, caracter, longitud):
    longitud_caracter = key.count(caracter)
    parte_clave = key[:longitud - longitud_caracter]
    claves = [parte_clave + "".join(i) for i in list(producto_cartesiano([chr(i) for i in range(65, 65+26)], repeat=longitud_caracter))]
    return claves

def cifrado_vigenere(texto, clave):
    resultado_final = []
    codigo = list(texto)
    j = 0

    for i, caracter in enumerate(codigo):
        if caracter.isalpha():
            codigo[i] = clave[(i + j) % len(clave)]
            resultado_final.append((ord(texto[i]) - ord(codigo[i])) % 26)
            j -= 1
        else:
            resultado_final.append(ord(caracter))

    for i, caracter in enumerate(codigo):
        if codigo[i].isalpha():
            resultado_final[i] = chr(resultado_final[i] + 65)
        else:
            resultado_final[i] = chr(resultado_final[i])

    return ''.join(resultado_final)

print("Bienvenido al desencriptador Vigenere")

texto = input('Ingresa el texto cifrado : ').upper()
tiene_clave = input('¿Tienes la clave (s/n)?: ')

if tiene_clave == "s":
    clave = input('Ingresa la clave : ').upper()
else:
    clave = None

if clave:
    print(f'Texto descifrado: {cifrado_vigenere(texto, clave)}')
else:
    print("No se puede desencriptar sin la clave. Si tienes parte de la clave, puedes proporcionarla a continuación.")
    pregunta = input('¿Conoces la longitud de la clave? (s/n)?: ')

    if pregunta == 's':
        longitud = int(input('Ingresa la longitud de la clave: '))
        lista_de_claves = generador_claves(texto, '?', longitud)

        for k in lista_de_claves:
            print(f'Para clave parcial {k} ==> Texto descifrado: {cifrado_vigenere(texto, k)}')
    else:
        abc = list("ABCDEFGHIJKHIJKLMNOPQRSTUVWXYZ")
        longitud = int(input('Ingresa la longitud de la clave: '))

        while True:
            clave_generada = ''.join(sample(abc, longitud))
            print(f"Para clave generada {clave_generada} ==> Texto descifrado: {cifrado_vigenere(texto, clave_generada)}")

            if input('¿Continuar (s/n) ... : ') == "n":
                break

