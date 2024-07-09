import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import *

import ScooterRentalAppUi

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ScooterRentalAppUi

class frontPage:
    root = ctk.CTk()
    root.title("ScooTeq App")
    root.iconbitmap("scooTecIcon.ico")
    root.geometry("500x350")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Was möchtest du machen?", font=("Helvetica", 15, "bold"))
    label.pack(pady=12, padx=10)

    ausleihen_button = ctk.CTkButton(master=frame, text="ausleihen", command=app.scooterAusleihen)
    ausleihen_button.pack(pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(master=frame, text="reservieren", command=app.scooterReservieren)
    reservieren_button.pack(pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(master=frame, text="Beenden", command=root.destroy)
    reservieren_button.pack(pady=12, padx=18)

frontPage.root.mainloop()

class secondPage:
    root = ctk.CTk()
    root.title("ScooTeq App")
    root.iconbitmap("scooTecIcon.ico")
    root.geometry("500x350")

    def update_time():
        exampleTimeField.configure(text=app.getCurrentTimeStamp())
        root.after(1000, update_time)

    exampleTimeField = ctk.CTkLabel(master=root, text="", font=("Calibri", 23))
    update_time()
    exampleTimeField.pack(pady=20)

secondPage.root.mainloop()