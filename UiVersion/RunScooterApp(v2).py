import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import *
import tkinter.messagebox as messagebox
import tkinter as tk
import ScooterRentalAppUi

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ScooterRentalAppUi

root = ctk.CTk()
root.title("ScooTeq App")
root.iconbitmap("UiVersion/scooTecIcon.ico")
root.geometry("550x380")

# Windows
frontPage = None
scooterUebersicht = None

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def update_time(updatingLabel):
    updatingLabel.configure(text=app.getCurrentTimeStamp())
    updatingLabel.after(1000, update_time, updatingLabel)


#fruehererZeitpunkt = selected_scooter.getAusleihZeitpunkt()
fruehererZeitpunkt = [8,30,0]
spaetererZeitpunkt = app.getCurrentTimeStamp()

def update_field(updatingLabel):
    global fruehererZeitpunkt
    spaetererZeitpunkt = app.getCurrentTimeStamp()
    time_difference = app.getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt)
    updatingLabel.configure(text=time_difference)
    updatingLabel.after(1000, update_field, updatingLabel)

def create_frontPage():
    global frontPage
    frontPage = ctk.CTkFrame(master=root)
    frontPage.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    upper_frame = ctk.CTkFrame(frontPage)
    upper_frame.grid(row=0, column=0, sticky='nsew', pady=5, padx=35)

    logo_image = Image.open("ScooTec3.png")  
    logo_image = logo_image.resize((70, 70), Image.LANCZOS)  
    logo_image = ImageTk.PhotoImage(logo_image)
    
    logo_label = tk.Label(upper_frame, image=logo_image)
    logo_label.image = logo_image
    logo_label.grid(row=0, column=0, pady=10, padx=10) 

    label = ctk.CTkLabel(upper_frame, text="Willkommen bei der SccTeq GmbH!", font=("Helvetica", 15, "bold"))
    label.grid(row=0, column=1, pady=12, padx=10)

    down_frame = ctk.CTkFrame(frontPage)
    down_frame.grid(row=1, column=0, sticky='nsew', pady=5, padx=5)

    label = ctk.CTkLabel(down_frame, text="Wähle eine Option:", font=("Helvetica", 15, "bold"))
    label.grid(row=0, column=0 , pady=12, padx=10)

    ausleihen_button = ctk.CTkButton(down_frame, text="ausleihen", command=app.scooterAusleihen)
    ausleihen_button.grid(row=0, column=1, pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(down_frame, text="reservieren", command=app.scooterReservieren)
    reservieren_button.grid(row=1, column=1, pady=12, padx=18)

    #switch_button1 = ctk.CTkButton(down_frame, text="Go to Frame 2", command=lambda: show_frame(scooterUebersicht))
    #switch_button1.grid(row=2, column=1, pady=12) 

    switch_button2 = ctk.CTkButton(down_frame, text="Scooter auswählen", command=lambda: show_frame(avalibleScooter))
    switch_button2.grid(row=2, column=1, pady=12)
    
    beenden_button  = ctk.CTkButton(down_frame, text="Beenden", command=root.destroy)
    beenden_button.grid(row=3, column=1, pady=12, padx=18)

   


def create_scooterUebersicht():
    global scooterUebersicht
    scooterUebersicht = ctk.CTkFrame(root)
    scooterUebersicht.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)
    
    dauerAusleihenField = ctk.CTkLabel(scooterUebersicht, text="", font=("Calibri", 23))
    dauerAusleihenField.pack(pady=20)

    update_field(dauerAusleihenField)

    exampleTimeField = ctk.CTkLabel(scooterUebersicht, text="", font=("Calibri", 23))
    exampleTimeField.pack(pady=20)

    update_time(exampleTimeField)

    switch_button2 = ctk.CTkButton(scooterUebersicht, text="Go to Frame 1", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=20)

def create_avalibleScooter():
    global avalibleScooter
    avalibleScooter = ctk.CTkFrame(root)
    avalibleScooter.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    left_frame = ctk.CTkFrame(avalibleScooter)
    left_frame.grid(row=0, column=0, sticky='nsew', pady=20, padx=20)

    scooter1Button = ctk.CTkButton(left_frame, text="Scooter 1", fg_color="green", command=lambda: show_frame(scooter1Uebersicht))
    scooter1Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter2Button = ctk.CTkButton(left_frame, text="Scooter 2", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter2Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter3Button = ctk.CTkButton(left_frame, text="Scooter 3", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter3Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter4Button = ctk.CTkButton(left_frame, text="Scooter 4", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter4Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter5Button = ctk.CTkButton(left_frame, text="Scooter 5", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter5Button.pack(side="top", anchor="w", pady=10, padx=10)

    right_frame = ctk.CTkFrame(avalibleScooter)
    right_frame.grid(row=0, column=1, sticky='nsew', pady=20, padx=20)

    scooter6Button = ctk.CTkButton(right_frame, text="Scooter 6", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter6Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter7Button = ctk.CTkButton(right_frame, text="Scooter 7", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter7Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter8Button = ctk.CTkButton(right_frame, text="Scooter 8", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter8Button.pack(side="top", anchor="w", pady=10, padx=10)

    scooter9Button = ctk.CTkButton(right_frame, text="Scooter 9", fg_color="green", command=lambda: show_frame(scooterUebersicht))
    scooter9Button.pack(side="top", anchor="w", pady=10, padx=10)

    roterButton = ctk.CTkButton(right_frame, text="Scooter 404", fg_color="red", command=popupNachricht)
    roterButton.pack(side="top", anchor="w", pady=10, padx=10)

    back_button_frame = ctk.CTkFrame(avalibleScooter)
    back_button_frame.grid(row=1, column=0, columnspan=2)

    switch_button2 = ctk.CTkButton(back_button_frame, text="Zurück", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=10)

def popupNachricht():
    messagebox.showinfo("Scooter nicht verfügbar", "Scooter nicht verfügbar, bitte einen grünen Scooter auswählen")    

def create_scooter1Uebersicht():
    global scooter1Uebersicht
    scooter1Uebersicht = ctk.CTkFrame(root)
    scooter1Uebersicht.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)
 
    exampleTimeField = ctk.CTkLabel(scooter1Uebersicht, text="", font=("Calibri", 23))
    exampleTimeField.pack(pady=20)
    update_time(exampleTimeField)
    zurueckButton = ctk.CTkButton(scooter1Uebersicht, text="Zurück", command=lambda: show_frame(avalibleScooter))
    zurueckButton.pack(pady=20)



def show_frame(frame):
    frame.tkraise()

def runApp():
    create_frontPage()
    create_scooterUebersicht()
    create_avalibleScooter()
    create_scooter1Uebersicht()
    show_frame(frontPage)
    root.mainloop()

while True:
    runApp()
