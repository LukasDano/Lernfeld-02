import tkinter as tk
from PIL import Image, ImageTk

# Mocking the ScooterRentalApp for demonstration purposes
class ScooterRentalApp:
    @staticmethod
    def hasReservierung():
        return False  # Change as needed for testing

    @staticmethod
    def scooterAusleihen():
        return "Scooter wurde ausgeliehen!"

    @staticmethod
    def datenZurAktuellenFahrt():
        return "Daten der aktuellen Fahrt werden angezeigt!"

    @staticmethod
    def scooterZurueckgeben():
        return "Scooter wurde zurückgegeben!"

    @staticmethod
    def scooterReservieren():
        return "Scooter wurde reserviert!"

    @staticmethod
    def uebersichtScooter():
        return "Übersicht der Scooter und Reservierungen!"

app = ScooterRentalApp()

# List of scooter IDs for selection
scooter_ids = ["Scooter 1", "Scooter 2", "Scooter 3", "Scooter 4"]

# Main application window
root = tk.Tk()
root.title("Digitale Scooter App")

# Frame for scooter selection
selection_frame = tk.Frame(root)
selection_frame.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(selection_frame, text="Wählen Sie einen Scooter aus:").pack()

selected_scooter = tk.StringVar(value="")

# Frame to show selected scooter and back icon
header_frame = tk.Frame(root)

current_scooter_label = tk.Label(header_frame, text="", font=("Helvetica", 16))
current_scooter_label.pack(side=tk.LEFT)

def back_to_selection():
    header_frame.pack_forget()
    options_frame.pack_forget()
    output_label.pack_forget()
    selection_frame.pack(side=tk.LEFT, padx=20, pady=20)
    selected_scooter.set("")

# Load the icon image and resize it
original_image = Image.open("back_icon.png")  # Replace with your icon file
resized_image = original_image.resize((30, 30), Image.LANCZOS)  # Resize the image
back_icon = ImageTk.PhotoImage(resized_image)

back_button = tk.Button(header_frame, image=back_icon, command=back_to_selection)
back_button.pack(side=tk.RIGHT)

def display_options(scooter_id):
    selected_scooter.set(scooter_id)
    current_scooter_label.config(text=f"Aktuell bearbeitest du: {selected_scooter.get()}")
    selection_frame.pack_forget()
    header_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
    options_frame.pack(side=tk.LEFT, padx=20, pady=20)
    output_label.pack(side=tk.RIGHT, padx=20, pady=20)

for scooter in scooter_ids:
    button = tk.Button(selection_frame, text=scooter, command=lambda s=scooter: display_options(s))
    button.pack(fill='x', pady=5)

# Frame for option buttons
options_frame = tk.Frame(root)

# Output label on the right side
output_label = tk.Label(root, text="Ergebnisse werden hier angezeigt", justify=tk.LEFT)

def update_output(text):
    output_label.config(text=text)

def on_exit():
    root.destroy()

# Buttons for options
buttons = [
    ("0. Beenden", on_exit),
    ("1. Scooter ausleihen", lambda: update_output(app.scooterAusleihen())),
    ("2. Daten der aktuellen Fahrt abfragen", lambda: update_output(app.datenZurAktuellenFahrt())),
    ("3. Scooter zurückgeben", lambda: update_output(app.scooterZurueckgeben())),
    ("4. Scooter reservieren", lambda: update_output(app.scooterReservieren())),
    ("5. Scooter Übersicht (Reservierungen)", lambda: update_output(app.uebersichtScooter())),
]

for (text, command) in buttons:
    button = tk.Button(options_frame, text=text, command=command)
    button.pack(fill='x', pady=5)

# set the size of the window (breite x hoehe )
root.geometry("650x400")
# Run the application
root.mainloop()
