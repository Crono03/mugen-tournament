import tkinter as tk

def create_locale_gui():
    # Creazione della finestra principale per la sezione "Locale"
    locale_window = tk.Tk()
    locale_window.title("Locale")

    # Imposta la grandezza predefinita della GUI e posiziona al centro
    width, height = 400, 300
    screen_width = locale_window.winfo_screenwidth()
    screen_height = locale_window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    locale_window.geometry(f"{width}x{height}+{x}+{y}")

    # Roba della gui
    label = tk.Label(locale_window, text="Benvenuto nella sezione Locale!")
    label.pack(pady=20)
    
    # Avvio del loop principale per la finestra "Locale"
    locale_window.mainloop()

# Esegui la funzione create_locale_gui() quando si esegue il file
if __name__ == "__main__":
    create_locale_gui()
