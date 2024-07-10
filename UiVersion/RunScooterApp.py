import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import *
import tkinter.messagebox as messagebox
import tkinter as tk
import ScooterRentalAppUi

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ScooterRentalAppUi.ScooterRentalApp()

root = ctk.CTk()
root.title("ScooTeq App")
root.iconbitmap("UiVersion/scooTecIcon.ico")
root.geometry("550x380")

def getUhrzeit():
    now = datetime.now()
    hours = int(now.strftime("%H"))
    minutes = int(now.strftime("%M"))
    seconds = int(now.strftime("%S"))

    return [hours, minutes, seconds]


# Windows
frontPage = None
scooterFahrtUebersicht = None
scooterReservierungsUebersicht = None

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def update_price(updatingLabel):
    currentScooter = app.getScooterById(app.bearbeiteterScooterId)

    timeDifference = app.getTimeDifferance(currentScooter.getAusleihZeitpunkt(), getUhrzeit())
    hours = timeDifference[0]
    minutes = timeDifference[1]
    seconds = getUhrzeit()[2]

    timeInMinutes = hours * 60 + minutes
    if seconds != 0:
        timeInMinutes += 1

    currentPrice = app.getPrice(timeInMinutes)
    currentScooter.setAktuellerPreis(currentPrice)

    updatingLabel.configure(text=f"Preis: {currentPrice}€")
    updatingLabel.after(1000, update_price, updatingLabel)

def update_rentTime(updatingLabel):
    currentScooter = app.getScooterById(app.bearbeiteterScooterId)

    time_difference = app.getTimeDifferance(currentScooter.getAusleihZeitpunkt(), getUhrzeit())

    hours_str = f"{time_difference[0]:02}"
    minutes_str = f"{time_difference[1]:02}"
    seconds_str = f"{time_difference[2]:02}"

    displayedTimeText = f"Dauer aktuelle Fahrt: {hours_str}:{minutes_str}:{seconds_str} h"
    updatingLabel.configure(text=displayedTimeText)
    updatingLabel.after(1000, update_rentTime, updatingLabel)

# Ui - Funktionen
def scooterAusleihenUi(id):
    global ausleihZeitpunkt 
    ausleihZeitpunkt = getUhrzeit()
    app.scooterAusleihen(id)
    show_frame(scooterFahrtUebersicht)

def create_frontPage():
    global frontPage
    frontPage = ctk.CTkFrame(master=root)
    frontPage.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    upper_frame = ctk.CTkFrame(frontPage)
    upper_frame.grid(row=0, column=0, sticky='nsew', pady=5, padx=35)

    logo_image = Image.open("UiVersion/scooTecLogo.png")  
    logo_image = logo_image.resize((70, 70), Image.LANCZOS)  
    logo_image = ImageTk.PhotoImage(logo_image)
    
    logo_label = tk.Label(upper_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=10, padx=10) 

    label = ctk.CTkLabel(upper_frame, text="Willkommen bei der ScooTeq GmbH!", font=("Helvetica", 15, "bold"))
    label.grid(row=0, column=1, pady=12, padx=10)

    down_frame = ctk.CTkFrame(frontPage)
    down_frame.grid(row=1, column=0, sticky='nsew', pady=5, padx=5)

    label = ctk.CTkLabel(down_frame, text="Wähle eine Option:", font=("Helvetica", 15, "bold"))
    label.grid(row=0, column=0 , pady=12, padx=10)

    ausleihen_button = ctk.CTkButton(down_frame, text="Ausleihen", command=lambda: show_frame(avalibleScooter))
    ausleihen_button.grid(row=0, column=1, pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(down_frame, text="Reservieren", command=lambda: show_frame(scooterReservierungsUebersicht))
    reservieren_button.grid(row=1, column=1, pady=12, padx=18)

    #switch_button1 = ctk.CTkButton(down_frame, text="Go to Frame 2", command=lambda: show_frame(scooterUebersicht))
    #switch_button1.grid(row=2, column=1, pady=12) 

    #switch_button2 = ctk.CTkButton(down_frame, text="Scooter auswählen", command=lambda: show_frame(avalibleScooter))
    #switch_button2.grid(row=2, column=1, pady=12)
    
    beenden_button  = ctk.CTkButton(down_frame, text="Beenden", command=root.destroy)
    beenden_button.grid(row=3, column=1, pady=12, padx=18)


def create_scooterFahrtUebersicht():
    global scooterFahrtUebersicht
    scooterFahrtUebersicht = ctk.CTkFrame(root)
    scooterFahrtUebersicht.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)
    
    dauerAusleihenField = ctk.CTkLabel(scooterFahrtUebersicht, text="", font=("Calibri", 23))
    dauerAusleihenField.pack(pady=20)

    update_rentTime(dauerAusleihenField)

    exampleTimeField = ctk.CTkLabel(scooterFahrtUebersicht, text="", font=("Calibri", 23))
    exampleTimeField.pack(pady=20)

    update_price(exampleTimeField)

    switch_button2 = ctk.CTkButton(scooterFahrtUebersicht, text="Home", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=20)

def create_scooterReservierungsUebersicht():
    global scooterReservierungsUebersicht
    scooterReservierungsUebersicht = ctk.CTkFrame(root)
    scooterReservierungsUebersicht.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)
    
    dauerAusleihenField = ctk.CTkLabel(scooterReservierungsUebersicht, text="", font=("Calibri", 23))
    dauerAusleihenField.pack(pady=20)

    update_rentTime(dauerAusleihenField)

    exampleTimeField = ctk.CTkLabel(scooterReservierungsUebersicht, text="", font=("Calibri", 23))
    exampleTimeField.pack(pady=20)

    update_price(exampleTimeField)

    switch_button2 = ctk.CTkButton(scooterReservierungsUebersicht, text="Go to Frame 1", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=20)

def create_avalibleScooterReservieren():
    global create_avalibleScooterReservieren
    create_avalibleScooterReservieren = ctk.CTkFrame(root)
    create_avalibleScooterReservieren.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    left_frame = ctk.CTkFrame(create_avalibleScooterReservieren)
    left_frame.grid(row=0, column=0, sticky='nsew', pady=20, padx=20)

    scooter1Button = ctk.CTkButton(left_frame, text="Scooter 1", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter1Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter2Button = ctk.CTkButton(left_frame, text="Scooter 2", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter2Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter3Button = ctk.CTkButton(left_frame, text="Scooter 3", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter3Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter4Button = ctk.CTkButton(left_frame, text="Scooter 4", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter4Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter5Button = ctk.CTkButton(left_frame, text="Scooter 5", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter5Button.pack(side="top", anchor="w", pady=10, padx=10)

    right_frame = ctk.CTkFrame(create_avalibleScooterReservieren)
    right_frame.grid(row=0, column=1, sticky='nsew', pady=20, padx=20)

    scooter6Button = ctk.CTkButton(right_frame, text="Scooter 6", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter6Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter7Button = ctk.CTkButton(right_frame, text="Scooter 7", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter7Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter8Button = ctk.CTkButton(right_frame, text="Scooter 8", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter8Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter9Button = ctk.CTkButton(right_frame, text="Scooter 9", fg_color="green", command=lambda: show_frame(scooterReservierungsUebersicht))
    scooter9Button.pack(side="top", anchor="w", pady=10, padx=10)

    roterButton = ctk.CTkButton(right_frame, text="Scooter 404", fg_color="red", command=popupNachricht)
    roterButton.pack(side="top", anchor="w", pady=10, padx=10)

    back_button_frame = ctk.CTkFrame(create_avalibleScooterReservieren)
    back_button_frame.grid(row=1, column=0, columnspan=2)

    switch_button2 = ctk.CTkButton(back_button_frame, text="Zurück", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=10)

def create_avalibleScooter():
    global avalibleScooter
    avalibleScooter = ctk.CTkFrame(root)
    avalibleScooter.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    left_frame = ctk.CTkFrame(avalibleScooter)
    left_frame.grid(row=0, column=0, sticky='nsew', pady=20, padx=20)

    scooter1Button = ctk.CTkButton(left_frame, text="Scooter 1", fg_color="green", command = lambda: scooterAusleihenUi(1))
    scooter1Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter2Button = ctk.CTkButton(left_frame, text="Scooter 2", fg_color="green", command = lambda: scooterAusleihenUi(2))
    scooter2Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter3Button = ctk.CTkButton(left_frame, text="Scooter 3", fg_color="green", command = lambda: scooterAusleihenUi(3))
    scooter3Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter4Button = ctk.CTkButton(left_frame, text="Scooter 4", fg_color="green", command = lambda: scooterAusleihenUi(4))
    scooter4Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter5Button = ctk.CTkButton(left_frame, text="Scooter 5", fg_color="green", command = lambda: scooterAusleihenUi(5))
    scooter5Button.pack(side="top", anchor="w", pady=10, padx=10)

    right_frame = ctk.CTkFrame(avalibleScooter)
    right_frame.grid(row=0, column=1, sticky='nsew', pady=20, padx=20)

    scooter6Button = ctk.CTkButton(right_frame, text="Scooter 6", fg_color="green", command = lambda: scooterAusleihenUi(6))
    scooter6Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter7Button = ctk.CTkButton(right_frame, text="Scooter 7", fg_color="green", command = lambda: scooterAusleihenUi(7))
    scooter7Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter8Button = ctk.CTkButton(right_frame, text="Scooter 8", fg_color="green", command = lambda: scooterAusleihenUi(8))
    scooter8Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter9Button = ctk.CTkButton(right_frame, text="Scooter 9", fg_color="green", command = lambda: scooterAusleihenUi(9))
    scooter9Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter10Button = ctk.CTkButton(right_frame, text="Scooter 10", fg_color="green", command = lambda: scooterAusleihenUi(10))
    scooter10Button.pack(side="top", anchor="w", pady=10, padx=10)

    back_button_frame = ctk.CTkFrame(avalibleScooter)
    back_button_frame.grid(row=1, column=0, columnspan=2)

    switch_button2 = ctk.CTkButton(back_button_frame, text="Zurück", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=10)

def popupNachricht():
    messagebox.showinfo("Scooter nicht verfügbar", "Scooter nicht verfügbar, bitte einen grünen Scooter auswählen")    



def show_frame(frame):
    frame.tkraise()

def runApp():
    create_frontPage()
    create_scooterFahrtUebersicht()
    create_avalibleScooter()
    create_avalibleScooterReservieren()
    show_frame(frontPage)
    root.mainloop()

runApp()
