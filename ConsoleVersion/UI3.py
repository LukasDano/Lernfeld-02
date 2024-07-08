import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime, timedelta

# Enhanced ScooterRentalApp for demonstration purposes
class ScooterRentalApp:
    def __init__(self):
        self.scooters = {f"Scooter {i+1}": None for i in range(4)}
        self.rental_price_per_minute = 0.10  # Example price per minute

    def hasReservierung(self):
        return any(self.scooters[scooter] is not None for scooter in self.scooters)

    def scooterAusleihen(self, scooter_id):
        if self.scooters[scooter_id] is None:
            self.scooters[scooter_id] = datetime.now()
            return f"{scooter_id} wurde ausgeliehen!"
        else:
            return f"{scooter_id} ist bereits ausgeliehen!"

    def datenZurAktuellenFahrt(self, scooter_id):
        if self.scooters[scooter_id] is None:
            return f"{scooter_id} ist nicht ausgeliehen."
        else:
            start_time = self.scooters[scooter_id]
            current_time = datetime.now()
            duration = current_time - start_time
            minutes = int(duration.total_seconds() / 60)
            price = minutes * self.rental_price_per_minute
            return f"Startzeit: {start_time.strftime('%H:%M:%S')}\nAktuelle Dauer: {minutes} Minuten\nPreis: {price:.2f} €"

    def scooterZurueckgeben(self, scooter_id):
        if self.scooters[scooter_id] is None:
            return f"{scooter_id} ist nicht ausgeliehen."
        else:
            start_time = self.scooters[scooter_id]
            current_time = datetime.now()
            duration = current_time - start_time
            minutes = int(duration.total_seconds() / 60)
            price = minutes * self.rental_price_per_minute
            self.scooters[scooter_id] = None
            return f"{scooter_id} wurde zurückgegeben.\nGesamtdauer: {minutes} Minuten\nGesamtpreis: {price:.2f} €"

    def scooterReservieren(self, scooter_id):
        return f"{scooter_id} wurde reserviert!"

    def uebersichtScooter(self):
        overview = ""
        for scooter, start_time in self.scooters.items():
            if start_time is None:
                overview += f"{scooter}: Verfügbar\n"
            else:
                duration = datetime.now() - start_time
                minutes = int(duration.total_seconds() / 60)
                price = minutes * self.rental_price_per_minute
                overview += f"{scooter}: Ausgeliehen\nDauer: {minutes} Minuten\nPreis: {price:.2f} €\n"
        return overview

# Initialize the app
app = ScooterRentalApp()

# List of scooter IDs for selection
scooter_ids = list(app.scooters.keys())

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
    current_scooter_label.config(text=f"Bearbeite: {selected_scooter.get()}")
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
    ("1. Scooter ausleihen", lambda: update_output(app.scooterAusleihen(selected_scooter.get()))),
    ("2. Daten der aktuellen Fahrt abfragen", lambda: update_output(app.datenZurAktuellenFahrt(selected_scooter.get()))),
    ("3. Scooter zurückgeben", lambda: update_output(app.scooterZurueckgeben(selected_scooter.get()))),
    ("4. Scooter reservieren", lambda: update_output(app.scooterReservieren(selected_scooter.get()))),
    ("5. Scooter Übersicht (Reservierungen)", lambda: update_output(app.uebersichtScooter())),
]

for (text, command) in buttons:
    button = tk.Button(options_frame, text=text, command=command)
    button.pack(fill='x', pady=5)

# Run the application
root.mainloop()
