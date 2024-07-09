import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import *
import pystray
from pystray import MenuItem as item
import threading
import sys


import ScooterRentalAppUi

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ScooterRentalAppUi

def close():
    root.destroy()

def runTheApp():
    root.geometry("650x400")
    root.mainloop()

def update_time():
    current_time = app.getCurrentTimeStamp()
    textField.configure(text=current_time)
    root.after(1000, update_time)

root = ctk.CTk()
root.title("ScooTeq App")
root.iconbitmap("scooTecIcon.ico")

textField = ctk.CTkLabel(root, text="", font=("Arial", 48))
textField.pack(pady=20)


# Frame for scooter selection
selection_frame = ctk.CTkFrame(root)

update_time()

if __name__ == "__main__":
    runTheApp()
