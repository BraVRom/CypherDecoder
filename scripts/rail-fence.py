def offset(par, railes, raíl):
    if raíl == 0 or raíl == railes - 1:
        return (railes - 1) * 2
    if par:
        return 2 * raíl
    else:
        return 2 * (railes - 1 - raíl)

def descifrarRailFence(cripto, railes):
    if str(railes).lower() == "s":  # Aseguramos que 'railes' sea tratado en minúsculas
        for i in range(round(len(cripto) / 2)):
            print(descifrarRailFence(cripto, i))
    else:
        railes = int(railes)
        matriz = [[" " for col in range(len(cripto))] for fila in range(railes)]
        leído = 0

        # Construir nuestra valla
        for raíl in range(railes):
            pos = offset(1, railes, raíl)
            par = 0

            if raíl == 0:
                pos = 0
            else:
                pos = int(pos / 2)

            while pos < len(cripto):
                if leído == len(cripto):
                    break

                matriz[raíl][pos] = cripto[leído]
                leído = leído + 1
                pos = pos + offset(par, railes, raíl)
                par = not par

        # Ahora devolvemos el mensaje descifrado
        descifrado = ""

        for x in range(len(cripto)):
            for y in range(railes):
                if matriz[y][x] != " ":
                    descifrado += matriz[y][x]

        return descifrado

texto_cifrado = input("Introduce el texto cifrado en rail-fence:\nEJEMPLO: Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6\n")
numero_railes = input("Introduce el número de raíles:\n(Si no sabes el número de raíles, introduce S, y aplicará fuerza bruta)\nEJEMPLO: 4\n")

resultado = descifrarRailFence(texto_cifrado, numero_railes)
print(resultado)

