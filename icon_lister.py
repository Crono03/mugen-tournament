import os

def list_icons_from_config(config_path):
    # Leggi il roster dal file config.txt, ignorando le prime 4 righe
    with open(config_path, 'r', encoding='utf-8') as config_file:
    
        mugen_path = config_file.readline().strip()
        for _ in range(3):
            next(config_file)
        
        # Leggi il resto del file e ottieni il roster
        roster_lines = [line.strip() for line in config_file.readlines()]

    print(f"Percorso di Mugen: {mugen_path}")

    # Costruisci il percorso completo della cartella "chars"
    chars_path = os.path.join(mugen_path, 'chars')
    print(f"Percorso di chars: {chars_path}")

    # Verifica se la cartella "chars" esiste
    if os.path.exists(chars_path):

        icon_names = []

        # Per ciascuna entry del roster, controlla la presenza di un file .def nella cartella "chars" e nelle sue sottocartelle
        for line in roster_lines:
            if line and not line.startswith(';'):
              
                character_name = line.rstrip('.def').lower()
                def_file_path = os.path.join(chars_path, f"{character_name}.def")

                # Cerca il file .def nella cartella "chars" e nelle sottocartelle
                found = False
                for root, dirs, files in os.walk(chars_path):
                    if f"{character_name}.def" in [file.lower() for file in files]:
                        found = True
                        
                        def_file_path = os.path.join(root, f"{character_name}.def")
                        print(f"File .def trovato per {character_name}: {def_file_path}")
                        break

                if found:
                    icon_names.append(character_name)
                else:
                    print(f"WARNING: Il file .def non esiste per {character_name} in {chars_path}")
    else:
        print(f"WARNING: La cartella 'chars' non esiste in {mugen_path}")
        icon_names = []

    return icon_names

if __name__ == "__main__":
    config_path = "config.txt"

    icons = list_icons_from_config(config_path)
    print("Icon names trovati:")
    for icon in icons:
        print(icon)
