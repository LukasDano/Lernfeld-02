import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import *

import ScooterRentalAppUi

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ScooterRentalAppUi

root = ctk.CTk()
root.title("ScooTeq App")
root.iconbitmap("UiVersion/scooTecIcon.ico")
root.geometry("500x350")

def getUhrzeit():
    now = datetime.now()
    hours = int(now.strftime("%H"))
    minutes = int(now.strftime("%M"))
    seconds = int(now.strftime("%S"))

    return [hours, minutes, seconds]

# Golbale Variablen
ausleihZeitpunkt = [0,0,0]
spaetererZeitpunkt = getUhrzeit()
currentPrice = 0

# Windows
frontPage = None
scooterUebersicht = None

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def update_price(updatingLabel):

    timeDifference = app.getTimeDifferance(ausleihZeitpunkt, getUhrzeit())
    hours = timeDifference[0]
    minutes = timeDifference[1]
    seconds = getUhrzeit()[2]

    timeInMinutes = hours * 60 + minutes
    if seconds != 0:
        timeInMinutes += 1

    currentPrice = app.getPrice(timeInMinutes)

    updatingLabel.configure(text=f"Preis: {currentPrice}€")
    updatingLabel.after(1000, update_price, updatingLabel)

def update_rentTime(updatingLabel):
    time_difference = app.getTimeDifferance(ausleihZeitpunkt, getUhrzeit())

    hours_str = f"{time_difference[0]:02}"
    minutes_str = f"{time_difference[1]:02}"
    seconds_str = f"{time_difference[2]:02}"

    displayedTimeText = f"Dauer aktuelle Fahrt: {hours_str}:{minutes_str}:{seconds_str} h"
    updatingLabel.configure(text=displayedTimeText)
    updatingLabel.after(1000, update_rentTime, updatingLabel)

def scooterAusleihenUi():
    global ausleihZeitpunkt 
    ausleihZeitpunkt = getUhrzeit()
    app.scooterAusleihen


def create_frontPage():
    global frontPage
    frontPage = ctk.CTkFrame(master=root)
    frontPage.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    label = ctk.CTkLabel(frontPage, text="Was möchtest du machen?", font=("Helvetica", 15, "bold"))
    label.pack(pady=12, padx=10)

    ausleihen_button = ctk.CTkButton(frontPage, text="ausleihen", command=scooterAusleihenUi)
    ausleihen_button.pack(pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(frontPage, text="reservieren", command=app.scooterReservieren)
    reservieren_button.pack(pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(frontPage, text="Beenden", command=root.destroy)
    reservieren_button.pack(pady=12, padx=18)

    switch_button1 = ctk.CTkButton(frontPage, text="Go to Frame 2", command=lambda: show_frame(scooterUebersicht))
    switch_button1.pack(pady=20)

def create_scooterUebersicht():
    global scooterUebersicht
    scooterUebersicht = ctk.CTkFrame(root)
    scooterUebersicht.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)
    
    dauerAusleihenField = ctk.CTkLabel(scooterUebersicht, text="", font=("Calibri", 23))
    dauerAusleihenField.pack(pady=20)

    update_rentTime(dauerAusleihenField)

    exampleTimeField = ctk.CTkLabel(scooterUebersicht, text="", font=("Calibri", 23))
    exampleTimeField.pack(pady=20)

    update_price(exampleTimeField)

    switch_button2 = ctk.CTkButton(scooterUebersicht, text="Go to Frame 1", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=20)

def show_frame(frame):
    frame.tkraise()

def runApp():
    create_frontPage()
    create_scooterUebersicht()
    show_frame(frontPage)
    root.mainloop()

while True:
    runApp()
