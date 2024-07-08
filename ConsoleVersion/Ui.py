import tkinter as tk
from tkinter import messagebox

# Mocking the ScooterRentalApp for demonstration purposes
class ScooterRentalApp:
    @staticmethod
    def hasReservierung():
        return False  # Change as needed for testing

    @staticmethod
    def scooterAusleihen():
        messagebox.showinfo("Scooter Ausleihen", "Scooter wurde ausgeliehen!")

    @staticmethod
    def datenZurAktuellenFahrt():
        messagebox.showinfo("Aktuelle Fahrt", "Daten der aktuellen Fahrt werden angezeigt!")

    @staticmethod
    def scooterZurueckgeben():
        messagebox.showinfo("Scooter Zurueckgeben", "Scooter wurde zurueckgegeben!")

    @staticmethod
    def scooterReservieren():
        messagebox.showinfo("Scooter Reservieren", "Scooter wurde reserviert!")

    @staticmethod
    def uebersichtScooter():
        messagebox.showinfo("Scooter Uebersicht", "Übersicht der Scooter und Reservierungen!")

app = ScooterRentalApp()

# Main application window
root = tk.Tk()
root.title("Digitale Scooter App")

# Reminder for reservation
if app.hasReservierung():
    reminder_label = tk.Label(root, text="- Reminder -", fg="red")
    reminder_label.pack()

    overview_button = tk.Button(root, text="Übersicht der Scooter", command=app.uebersichtScooter)
    overview_button.pack()

# Options section
options_frame = tk.Frame(root)
options_frame.pack(pady=20)

tk.Label(options_frame, text="Optionen:").pack()

def on_exit():
    root.destroy()

# Buttons for options
buttons = [
    ("0. Beenden", on_exit),
    ("1. Scooter ausleihen", app.scooterAusleihen),
    ("2. Daten der aktuellen Fahrt abfragen", app.datenZurAktuellenFahrt),
    ("3. Scooter zurueckgeben", app.scooterZurueckgeben),
    ("4. Scooter reservieren", app.scooterReservieren),
    ("5. Scooter Uebersicht (Reservierungen)", app.uebersichtScooter),
]

for (text, command) in buttons:
    button = tk.Button(options_frame, text=text, command=command)
    button.pack(fill='x', pady=5)

# Run the application
root.mainloop()
