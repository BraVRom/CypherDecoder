abc = "abcdefghijklmnopqrstuvwxyz"

# Solicitar entrada al usuario
txt = input("Ingresa una serie de números separados por espacios y presiona Enter: ")

txtArr = txt.split(" ")  # Divide la entrada en una lista de números separados por espacios

sol = ""  # Inicializa una cadena vacía para almacenar la solución

for number in txtArr:
    sol += abc[int(number) - 1]  # Convierte el número en una letra y lo agrega a la solución

print("La cadena convertida es:", sol)  # Imprime la solución completa

