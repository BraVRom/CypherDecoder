#!/bin/bash

# Función para comprobar si es Base64 válido
is_base64() {
  if [[ "$1" =~ ^[A-Za-z0-9+/]*=*$ ]]; then
    return 0 # Válido
  else
    return 1 # No válido
  fi
}

# Función para descifrar Base64
decode_base64() {
  echo "$1" | base64 -d
}

while true; do
  read -p "Introduce una cadena Base64: " cadena_base64

  if is_base64 "$cadena_base64"; then
    resultado=$(decode_base64 "$cadena_base64")
    echo "Resultado: $resultado"
  else
    echo "Eso no es una cadena Base64 válida."
  fi

  read -p "¿Repetimos? escribe 'n', 's' para salir): " respuesta
  respuesta_lower=$(echo "$respuesta" | tr '[:upper:]' '[:lower:]')
  
  case "$respuesta_lower" in
    no | n)
      break
      ;;
    yes | y | s)
      continue
      ;;
    *)
      echo "Respuesta no válida, continuando..."
      ;;
  esac
done

