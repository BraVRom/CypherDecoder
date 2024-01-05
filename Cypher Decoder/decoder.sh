#!/bin/bash

# Cambiar al directorio de "scripts/, importante"
cd "$(dirname "$0")/scripts"

# Permisos hex.sh y base64.sh
chmod +x "hex.sh"
chmod +x "base64.sh"

# Directorios
scripts_directory="."

# Lista
scripts=("ascii-code.py" "base64.sh" "hex.sh" "md5.py" "modular-inverse.py" "modular.py" "posicionAlf.py" "rail-fence.py" "rot.py" "sha256.py" "sha512.py" "transposition.py" "vigenere.py" "xor.py")

# Muestra los scripts disponibles
show_scripts() {
  clear  # Limpiar el terminal
  echo -e "\e[91m"
  echo "          
  ▒█▀▀█ █░░█ █▀▀█ █░░█ █▀▀ █▀▀█ 　 █▀▀▄ █▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 　 ▀█░█▀ ▄█░ 
  ▒█░░░ █▄▄█ █░░█ █▀▀█ █▀▀ █▄▄▀ 　 █░░█ █▀▀ █░░ █░░█ █░░█ █▀▀ █▄▄▀ 　 ░█▄█░ ░█░ 
  ▒█▄▄█ ▄▄▄█ █▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ 　 ▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀ 　 ░░▀░░ ▄█▄                                                              "
  echo -e "\e[92m                             By BraVRom - Github                  "
  echo -e "\e[0m                                   "
  echo "Scripts decodificadores:"
  echo "----------------"
  for ((i=0; i<${#scripts[@]}; i++)); do
    filename="${scripts[$i]}"
    filename_no_extension="${filename%.*}"  # Elimina extensión de archivitos
    filename_capitalized="$(tr '[:lower:]' '[:upper:]' <<< "${filename_no_extension:0:1}")${filename_no_extension:1}"  # Capitalizar la primera letra
    echo "$(($i + 1)). $filename_capitalized"
  done | column -t
}

# Ejecutar un script
run_script() {
  script_name="${scripts[$1 - 1]}"
  if [ -f "$scripts_directory/$script_name" ]; then
    clear  # Si lees esto pues Dragon ball rap
    echo "Executing $script_name..."
    echo ""
    if [ "$script_name" == "base64.sh" ] || [ "$script_name" == "hex.sh" ]; then
      bash "$scripts_directory/$script_name"
    else
      python3 "$scripts_directory/$script_name"
    fi
    echo ""
  else
    echo "$script_name no existe en la carpeta $scripts_directory."
    read -n1 -r -p "Presiona cualquier tecla para volver."
  fi
}


# Menú principal
while true; do
  show_scripts
  echo ""
  read -p "Choose (1-${#scripts[@]}) or 0 to exit: " choice

  if [ "$choice" == "0" ] || [ "$choice" == "clear" ] || [ "$choice" == "exit" ]; then
    echo "Exiting..."
    break
  elif [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 1 ] && [ "$choice" -le ${#scripts[@]} ]; then
    run_script "$choice"
  elif [ "$choice" == "br4hx" ]; then
    # Easter egg sisisisisi
    clear  
    sleep 1  
echo -e "\e[90m⠀⠀⠀⠀⠀       ⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠙⠻⢶⣄⡀⠀⠀⠀⢀⣤⠶⠛⠛⡇⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⣙⣿⣦⣤⣴⣿⣁⠀⠀⣸⠇⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣿⣿⣿⣿⣿⣷⣌⠋⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡈⢻⣿⡟⢁⣠⣾⣿⣦⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠘⣿⠃⣿⣿⣿⣿⡏⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠛⣰⠿⣆⠛⠁⠀⡀⠀⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣦⠀⠘⠛⠋⠀⣴⣿⠁⠀⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣏⠀⠀⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠾⢿⣿⠀⠀⠀⠀⠀⠀"
echo -e "⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⡥⠄⠀⠀⠀⠀⠉⢻⣄⠀⠀⠀⠀⠀"
echo -e "⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣁⣤⣀⣀⣤⣤⣤⣤⣄⣿⡄⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀"
echo -e "⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\e[0m"

    sleep 2
echo "A hard-working brain will do things right,"
sleep 2
echo "      a free brain will do brilliant things."
sleep 2
echo "______________________________________"
echo ""
    read -n1 -r -p "Press any key to return..."
  else
    echo "Opción inválida, escoge otra opción."
    echo ""
    read -n1 -r -p "Pulsa cualquier tecla para volver."
  fi
done

