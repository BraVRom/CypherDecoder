import itertools
import subprocess

def descifrar_transposicion(texto_cifrado, num_caracteres, max_permutaciones_a_mostrar=100):
    
    if num_caracteres == "S":
        for i in range(2, round(len(texto_cifrado) / 2)):
            print(descifrar_transposicion(texto_cifrado, i, max_permutaciones_a_mostrar))
    else:
        num_caracteres = int(num_caracteres)
        unidades = [texto_cifrado[i:i + num_caracteres] for i in range(0, len(texto_cifrado), num_caracteres)]
        permutaciones = ["".join(p) for u in unidades for p in itertools.permutations(u)]
        num_permutaciones_primer_elemento = len(list(itertools.permutations(unidades[0])))

        with open('scripts/permutaciones.txt', 'w') as f:
            for i, p in enumerate(permutaciones):
                if i >= max_permutaciones_a_mostrar:
                    break  # Detener la generación de permutaciones después de un límite
                f.write(p + '\n')  # Guardar cada permutación en el archivo permutaciones.txt

        print(f"Las primeras {max_permutaciones_a_mostrar} permutaciones se han guardado en 'scripts/permutaciones.txt'.")
        subprocess.run(["cat", "scripts/permutaciones.txt"])

        return permutaciones[:max_permutaciones_a_mostrar]

print(
descifrar_transposicion(
    input("Introduce el texto cifrado\n    EJEMPLO: heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2\n    "),
    input("Ingresa el número de letras por bloque\n    EJEMPLO: 3\n    "),
    10  # Límite de permutaciones a mostrar
))

input("Presiona Enter para salir...")

