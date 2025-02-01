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
        self.mw.title("Salary Prediction")  #Set the Title Name
        self.mw.geometry("800x600") #Set the windows size
        self.mw.configure(bg = "skyblue") #Set the window background color
        
        self.value = 0  #default value 
        
        self.top_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.top_frame.grid(row=0, column = 0, sticky="nsew")
        
        self.top_left_frame = tk.Frame(self.top_frame,bg = 'sky blue')
        self.top_left_frame.grid(row = 0,column = 0, sticky = "nsew")

        self.top_middle_frame = tk.Frame(self.top_frame,bg = 'sky blue')
        self.top_middle_frame.grid(row = 0,column = 1, sticky = "nsew")
        
        self.top_right_frame = tk.Frame(self.top_frame,bg = 'sky blue')
        self.top_right_frame.grid(row = 0,column = 2, sticky = "nsew")
        
        self.bottom_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.bottom_frame.grid(row=1, column = 0, sticky="nsew")
        
        self.bottom_left_frame = tk.Frame(self.bottom_frame, bg = 'sky blue')
        self.bottom_left_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.bottom_right_frame = tk.Frame(self.bottom_frame, bg = 'sky blue')
        self.bottom_right_frame.grid(row = 0, column = 1, sticky = "nsew")
        
        #Label
        self.Head_Title = tk.Label(self.top_middle_frame, text = " Salary Prediction Center", font=("times new roman", 14,"bold"), bg = "sky blue")
        self.Head_Title.grid(row=0, column = 4, sticky="nsew")
        
        #Image on the page 
        #img = Image.open("Salary.png")
        #img = ImageTk.PhotoImage(img)
        #self.Login_Image = tk.Label(self.top_middle_frame, image = img, bg = "skyblue")
        #self.Login_Image.image = img
        #self.Login_Image.grid(row=1, column = 4, sticky="nsew")
        
        #Label
        self.Company_name = tk.Label(self.bottom_left_frame, text = "Company Name", bg = "sky blue")
        self.Company_name.grid(row=1, column = 0, sticky="e")
        
        #Entry
        self.company_entry = tk.Entry(self.bottom_right_frame, size=20)
        self.company_entry.grid(row=1, column=1)
        
        #Label
        self.Rating = tk.Label(self.bottom_left_frame, text = "Rating", bg = "sky blue")
        self.Rating.grid(row=2, column = 0, sticky="e")
        
        tk.mainloop()

if __name__=='__main__':
    app = New_User()
    app.mw.mainloop