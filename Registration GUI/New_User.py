import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pydotplus


class New_User:
    def __init__(self):
        self.mw = tk.Tk() #Create the main window
        self.mw.iconphoto(True,tk.PhotoImage(file = "S.png"))  #Set the window icon
        self.mw.title("New User Registration")  #Set the Title Name
        self.mw.geometry("600x300") #Set the windows size
        self.mw.configure(bg = "skyblue") #Set the window background color
        
        self.value = 0  #default value 
        
        self.top_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.top_frame.grid(row = 0,column = 0,sticky = "nsew")

        self.mid_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.mid_frame.grid(row = 0, column = 1, sticky = 'nsew')
        
        #Image on the page 
        img = Image.open("Registration.png")
        img = ImageTk.PhotoImage(img)
        self.Login_Image = tk.Label(self.top_frame, image = img, bg = "skyblue")
        self.Login_Image.image = img
        self.Login_Image.grid(row = 3, column = 0, sticky = 'e')
        
        #Label
        self.Username = tk.Label(self.mid_frame,text = "Username", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Username.grid(row=1, column=0, padx=4, pady=4, sticky='e')
                
        #Text Entry
        self.Username_Entry = tk.Entry(self.mid_frame)
        self.Username_Entry.grid(row=1, column=1, padx=4, pady=4, sticky = 'e')
        
        #Label
        self.First_Name = tk.Label(self.mid_frame,text = "First Name", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.First_Name.grid(row=2, column=0, padx=4, pady=4, sticky='e')
        
        #Text Entry
        self.First_Name_Entry = tk.Entry(self.mid_frame)
        self.First_Name_Entry.grid(row=2, column=1, padx=4, pady=4, sticky  = 'e')
        
        #Label
        self.Middle_Name = tk.Label(self.mid_frame,text = "Middle Name", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Middle_Name.grid(row=3, column=0, padx=4, pady=4, sticky='e')

        #Text Entry
        self.Middle_Name_Entry = tk.Entry(self.mid_frame)
        self.Middle_Name_Entry.grid(row=3, column=1, padx=4, pady=4, sticky  = 'e')
        
        #Label
        self.Last_Name = tk.Label(self.mid_frame,text = "Last Name", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Last_Name.grid(row=4, column=0, padx=4, pady=4, sticky='e')

        #Text Entry
        self.Last_Name_Entry = tk.Entry(self.mid_frame)
        self.Last_Name_Entry.grid(row=4, column=1, padx=4, pady=4, sticky  = 'e')

        #Label
        self.Date_of_Birth = tk.Label(self.mid_frame,text = "Date of Birth", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Date_of_Birth.grid(row=5, column=0, padx=4, pady=4, sticky='e')

        #Text Entry
        self.Date_of_Birth_Entry = DateEntry(self.mid_frame, date_pattern = "yyyy-mm-dd")
        self.Date_of_Birth_Entry.grid(row=5, column=1, padx=4, pady=4, sticky = 'e')
        
        #Label
        self.New_Password = tk.Label(self.mid_frame,text = "New Password", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.New_Password.grid(row=6, column=0, padx=4, pady=4, sticky='e')
    
        
        #Text Entry
        self.New_Password_Entry = tk.Entry(self.mid_frame, show = '*')
        self.New_Password_Entry.grid(row=6, column=1, padx=4, pady=4, sticky = 'e')
        
        #Label
        self.Confirm_New_Password = tk.Label(self.mid_frame,text = "Confirm Password", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Confirm_New_Password.grid(row=7, column=0, padx=4, pady=4, sticky='e')

        #Text Entry
        self.Confirm_New_Password_Entry = tk.Entry(self.mid_frame)
        self.Confirm_New_Password_Entry.grid(row=7, column=1, padx=4, pady=4, sticky = 'e')
        
        #Button
        self.Registration_Button = tk.Button(self.mid_frame, text = "Register", bg = 'light green', command = self.output)
        self.Registration_Button.grid(row=8, column=1, padx=4, pady=4,sticky = 'w')
        
        #Back Button
        self.Back_Button = tk.Button(self.top_frame, text = "Back", bg = 'light green')
        self.Back_Button.grid(row=0, column=0, padx=4, pady=4,sticky = 'ne')
        tk.mainloop()
        
    def output(self):
        
        client = MongoClient("mongodb://localhost:27017/")
        db = client['Salary_Prediction']
        collection = db['Login_User']
        
        print(self.Username_Entry.get())
        print(self.First_Name_Entry.get())
        print(self.Middle_Name_Entry.get())
        print(self.Last_Name_Entry.get())
        print(self.Date_of_Birth_Entry.get())
        print(self.New_Password_Entry.get())
        print(self.Confirm_New_Password_Entry.get())
        
        username = self.Username_Entry.get()
        first_name = self.First_Name_Entry.get()
        middle_name = self.Middle_Name_Entry.get()
        last_name = self.Last_Name_Entry.get()
        Date_of_Birth = self.Date_of_Birth_Entry.get()
        new_password = self.New_Password_Entry.get()
        confirm_password = self.Confirm_New_Password_Entry.get()
        
        if not(username and first_name and middle_name and last_name and Date_of_Birth and new_password and confirm_password):
            messagebox.showwarning(" Please fill all the required details")
        elif new_password == confirm_password:
            input = {
                "Username" : username,
                "First Name": first_name,
                'Middle Name': middle_name,
                'Last Name':last_name,
                'Date of Birth':Date_of_Birth,
                'New Password':new_password,
                'Confirm Password':confirm_password
            }
            result = collection.insert_one(input)
            print("User Registration ID:", result.inserted_id)
            messagebox.showinfo("Page will shift to the login page", parent=self.mw)
        else:
            print("Password do not match. Please try again!!!")
            messagebox.showwarning("Password do not match. Please try again!!!", parent=self.mw)

if __name__=='__main__':
    app = New_User()
    app.mw.mainloop