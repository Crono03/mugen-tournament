import tkinter as tk
from tkinter import PhotoImage
from locale import create_locale_gui 
from fetcher import get_mugen_path



def create_menu():
    def button_click(button_number):
        if button_number == 1:
            # Se il pulsante "Locale (8)" viene premuto, distruggi la finestra corrente e carica la GUI di "Locale"
            root.destroy()
            create_locale_gui()

    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Applicazione con GUI")

    # Esegui il fetcher dei dati
    mugen_path = get_mugen_path()

    # Imposta la grandezza predefinita della GUI e posiziona al centro
    width, height = 640, 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

   
    #titolo
    image_path = 'title.png'
    original_img = PhotoImage(file=image_path)
    resized_img = original_img.subsample(1, 1)

    # Creazione di una label con il titolo
    label_image = tk.Label(root, image=resized_img)
    label_image.photo = resized_img 
    label_image.pack(pady=10, anchor="center")

    # Creazione di una label per il testo
    label_text = tk.Label(root, text="Seleziona il numero di partecipanti")
    label_text.pack(pady=5, anchor="center")

    # Creazione del pulsante "Locale (8)" che chiama la funzione button_click(1) quando viene premuto
    button_width = 15
    button_values = [8, 16, 32, 64]
    button_texts = [f"{regione}\n({valore})" for regione, valore in zip(["Locale", "Regionale", "Nazionale", "Mondiale"], button_values)]
    for i, text in enumerate(button_texts, start=1):
        button = tk.Button(root, text=text, width=button_width, command=lambda i=i: button_click(i))
        button.pack(pady=5)

    
    root.lift()
    root.mainloop()
