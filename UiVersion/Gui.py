import tkinter
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

def button1_function():
    print("Scooter ausgeliehen")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, text="Scooter ausleihen", corner_radius=10, command=button1_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def button2_function():
    print("Scooter reserviert")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, text="Scooter reservieren", corner_radius=10, command=button2_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.LEFT)




root_tk.mainloop()