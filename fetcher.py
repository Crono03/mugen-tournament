import tkinter as tk
from tkinter import filedialog
import os
from icon_lister import list_icons_from_config


config_file_path = "config.txt"


def get_mugen_path():
    global config_file_path

    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as file:
            mugen_path = file.readline().strip()  # Ricerca del path di mugen
    else:
        # Se il file di configurazione non esiste, chiedi all'utente di selezionare la cartella contenente mugen.exe
        root = tk.Tk()
        root.withdraw()


        mugen_exe_path = filedialog.askopenfilename(
            title="Seleziona il file .exe di Mugen",
            filetypes=[("File .exe", "*.exe")],
        )

        # estrazione directory in base all'exe
        mugen_path = os.path.dirname(mugen_exe_path)

        # Fix orientamento delle /
        mugen_path = mugen_path.replace("/", "\\")

        # Salva il percorso in un file di configurazione
        with open(config_file_path, "w") as file:
            file.write(f"{mugen_path}\n")

    # Leggi e aggiorna select.def ad ogni avvio
    fetch_and_update_config(mugen_path)

     # Esegui il lister degli icon names
    list_icons_from_config(config_file_path)


    return mugen_path

def fetch_and_update_config(mugen_path):
    # Costruisci il percorso completo del file select.def
    select_def_path = os.path.join(mugen_path, 'data', 'select.def')
    print(f"Percorso di select.def: {select_def_path}")

    # Verifica se il file select.def esiste
    if os.path.exists(select_def_path):
        # Leggi le righe dal file select.def dalla 73 alla 136 - limite hard coded visto che il numero dei personaggi non sarà dinamico
        #per ora
        selected_lines = []
        with open(select_def_path, 'r', encoding='utf-8') as select_def_file:
            lines = select_def_file.readlines()
            selected_lines = lines[72:135]  # 73-136

        
        print("Righe di select.def:")
        for line in selected_lines:
            print(line.strip())

        
    config_path = config_file_path

    # Stampa il percorso di config.txt nella console
    print(f"Percorso di config.txt: {config_path}")

    # Leggi il contenuto esistente del file config.txt
    with open(config_path, 'r', encoding='utf-8') as existing_config_file:
        existing_lines = existing_config_file.readlines()

    # Sovrascrivi il contenuto del file config.txt dalla terza riga in poi con il nuovo roster sotto la dicitura [Roster]
    with open(config_path, 'w', encoding='utf-8') as config_file:
        config_file.writelines(existing_lines[:2])
        config_file.write("\n")
        config_file.write("[Roster]\n")
        config_file.writelines(selected_lines)

    print("Roster scritto correttamente nel file config.txt.")

    
   


if __name__ == "__main__":
    mugen_path = get_mugen_path()
    print(f"Il percorso di Mugen è: {mugen_path}")