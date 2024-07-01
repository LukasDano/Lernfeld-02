import tkinter as tk
from tkinter import messagebox
import datetime

class ScooterRental:
    def __init__(self, rate_per_minute=0.15):
        self.rate_per_minute = rate_per_minute
        self.start_time = None
        self.end_time = None
    
    def start_rental(self):
        if self.start_time is None:
            self.start_time = datetime.datetime.now()
            return f"Scooter ausgeliehen um: {self.start_time}"
        else:
            return "Scooter ist bereits ausgeliehen."
    
    def end_rental(self):
        if self.start_time is not None:
            self.end_time = datetime.datetime.now()
            total_time, total_cost = self.calculate_total()
            self.start_time = None
            self.end_time = None
            return f"Scooter zurückgegeben um: {self.end_time}\nGesamtfahrzeit: {total_time:.2f} Minuten\nGesamtpreis: {total_cost:.2f} Euro"
        else:
            return "Scooter wurde noch nicht ausgeliehen."
    
    def calculate_total(self):
        if self.start_time and self.end_time:
            total_time = self.end_time - self.start_time
            total_minutes = total_time.total_seconds() / 60
            total_cost = total_minutes * self.rate_per_minute
            return total_minutes, total_cost
        else:
            return 0, 0
    
    def current_price(self):
        if self.start_time:
            current_time = datetime.datetime.now()
            current_duration = current_time - self.start_time
            current_minutes = current_duration.total_seconds() / 60
            current_cost = current_minutes * self.rate_per_minute
            return f"Aktueller Preis: {current_cost:.2f} Euro"
        else:
            return "Scooter wurde noch nicht ausgeliehen."

class ScooterRentalApp:
    def __init__(self, root):
        self.rental = ScooterRental()
        
        self.root = root
        self.root.title("Scooter Verleih")
        
        self.start_button = tk.Button(root, text="Ausleihen", command=self.start_rental)
        self.start_button.pack(pady=5)
        
        self.end_button = tk.Button(root, text="Ausleihen beenden", command=self.end_rental)
        self.end_button.pack(pady=5)
        
        self.price_button = tk.Button(root, text="Preis aktuell", command=self.current_price)
        self.price_button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)
    
    def start_rental(self):
        result = self.rental.start_rental()
        self.result_label.config(text=result)
    
    def end_rental(self):
        result = self.rental.end_rental()
        self.result_label.config(text=result)
    
    def current_price(self):
        result = self.rental.current_price()
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScooterRentalApp(root)
    root.mainloop()
