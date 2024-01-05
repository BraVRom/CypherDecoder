#!/bin/bash

# Solicita que ingrese hexadecimal
read -p "Ingresa el hexadecimal: " hex_string

# Verifica si la entrada es una cadena hexadecimal válida
if [[ ! "$hex_string" =~ ^[0-9a-fA-F]+$ ]]; then
    echo "Entrada no válida. Debes ingresar una cadena hexadecimal válida."
    exit 1
fi

# Convertir hexadecimal a texto
original_text=$(echo -n "$hex_string" | xxd -r -p)

if [ -n "$original_text" ]; then
    echo "Texto original: $original_text"
else
    echo "No se pudo convertir el hexadecimal a texto."
fi

