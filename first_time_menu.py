import tkinter as tk
from tkinter import filedialog
import os
from menu import create_menu

def get_mugen_path():
    config_file_path = "config.txt"

    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as file:
            mugen_path = file.read()
    else:
        root = tk.Tk()
        root.withdraw()

        mugen_path = filedialog.askopenfilename(
            title="Seleziona il file .exe di Mugen",
            filetypes=[("File .exe", "*.exe")],
        )

        with open(config_file_path, "w") as file:
            file.write(mugen_path)

    return mugen_path

def create_first_time_menu():
    root = tk.Tk()
    root.title("Prima Esecuzione")

    label = tk.Label(root, text="Benvenuto alla prima esecuzione!\nSeleziona il percorso di Mugen:")
    label.pack(pady=10)

    mugen_path = get_mugen_path()

    label_result = tk.Label(root, text=f"Il percorso di Mugen è: {mugen_path}")
    label_result.pack(pady=10)

    button_continue = tk.Button(root, text="Continua", command=root.destroy)
    button_continue.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_first_time_menu()
    create_menu()
