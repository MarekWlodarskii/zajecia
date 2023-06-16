import customtkinter as ctk
from datetime import date, timedelta

class Hotel(object):
    
    def Rezerwacja(self):
        self.ClearFrame()
        
        self.back = ctk.CTkButton(self.menu, text = "Powrot", width = 50, height = 30, font=("", 25), command = self.BuildMenu)
        self.back.grid(row=0, column=0)
        
        self.bedInfo = ctk.CTkLabel(master=self.menu, text="Ilosc lozek")
        self.bedInfo.grid(row=2, column=0, padx=10, pady=10)
        
        self.bed = ctk.CTkComboBox(self.menu, values = ['1', '2', '3'])
        self.bed.grid(row=2, column=1, padx=10, pady=10)
        
        self.bedInfo = ctk.CTkLabel(master=self.menu, text="Od kiedy")
        self.bedInfo.grid(row=3, column=0, padx=10, pady=10)
        
        self.dates = [str(date.today())]
        
        for x in range(1,20):
            self.dates.append(str((date.today()+timedelta(days=x)).isoformat()))
            
        self.bed = ctk.CTkComboBox(self.menu, values = self.dates)
        self.bed.grid(row=3, column=1, padx=10, pady=10)
        
        self.howLongInfo = ctk.CTkLabel(master=self.menu, text="Na ile dni")
        self.howLongInfo.grid(row=4, column=0, padx=10, pady=10)
        
        self.howLong = ctk.CTkEntry(self.menu)
        self.howLong.grid(row=4, column=1)
    
    def ClearFrame(self):
        for widgets in self.menu.winfo_children():
            widgets.destroy()
    
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.menu = ctk.CTk()
        self.menu.geometry("700x400")
        
        self.menu.title("Menu")
        self.BuildMenu()
        self.menu.mainloop()
    
    def BuildMenu(self):
        self.ClearFrame()
        
        self.frame = ctk.CTkFrame(master = self.menu)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.reserve = ctk.CTkButton(self.frame, text = "Dokonaj Rezerwacji", width = 300, height = 50, font=("", 25), command = self.Rezerwacja)
        self.reserve.pack(pady=(20, 20))
        
        self.cancel = ctk.CTkButton(self.frame, text = 'Anuluj Rezerwacje', width = 300, height = 50, font=("", 25))
        self.cancel.pack(pady=(0, 20))
        
    
    
Hotel()