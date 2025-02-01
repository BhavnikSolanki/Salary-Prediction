import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pydotplus

class Login:
    def __init__(self):
        self.mw = tk.Tk() #Create the main window
        self.mw.iconphoto(True,tk.PhotoImage(file = "S.png"))  #Set the window icon
        self.mw.title("Salary Prediction")  #Set the Title Name
        self.mw.geometry("300x236") #Set the windows size
        self.mw.configure(bg = "skyblue") #Set the window background color
        
        self.value = 0  #default value 

        #Create three frames to Organize the UI elements
        self.top_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.top_frame.pack()

        self.mid_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.mid_frame.pack()

        self.bottom_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.bottom_frame.pack()

        #Image on the page 
        img = Image.open("Login_Page_Img.png")
        img = ImageTk.PhotoImage(img)
        self.Login_Image = tk.Label(self.top_frame, image = img, bg = "skyblue")
        self.Login_Image.image = img
        self.Login_Image.pack()

        #Label
        self.Username = tk.Label(self.top_frame,text = "Username", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Username.pack(side = "left",padx = 4, pady = 4)

        #Text Entry
        self.Username_Entry = tk.Entry(self.top_frame)
        self.Username_Entry.pack(side = "right",padx = 4, pady = 4)

        #Label
        self.Password = tk.Label(self.mid_frame,text = "Password", bg = "skyblue",font = ('times new roman',12,'bold'))
        self.Password.pack(side = "left",padx = 4, pady = 4)

        #Text Entry
        self.Password_Entry = tk.Entry(self.mid_frame, show = "*")
        self.Password_Entry.pack(side = "right",padx = 4, pady = 4)

        #Login, Forgot and New Registration Button 
        self.Login_Button = tk.Button(self.bottom_frame,text = "Login", command = self.Logined)
        self.Login_Button.pack(side = "left", padx = 4,pady = 5)

        self.New_User_Button = tk.Button(self.bottom_frame,text = "New User",command = self.Newuser)
        self.New_User_Button.pack(side = "left",padx = 4, pady = 5)

        #Label for Forgot Password
        self.Forgot_Pwd_Text = tk.Label(self.mw,text = "Forgot Password", bg = 'skyblue', cursor ='hand2')
        self.Forgot_Pwd_Text.pack(side = "bottom",padx = 4, pady = 7)
        self.Forgot_Pwd_Text.bind('<Button-1>', self.forgot_pwd)
        
        tk.mainloop()
        
    def forgot_pwd(self,event):
        print("Forgot Password clicked")
    
    def Logined(self):
        #userdata = self.Username_Entry.get()
        #passdata = self.Password_Entry.get()

        if self.Username_Entry.get() == '' or self.Password_Entry.get() == '':
            messagebox.showerror("Error!!!, All Field are required",parent=self.mw)
        else:
            try:
                client = MongoClient("mongodb://localhost:27017/")
                db = client['Salary_Prediction']
                collection = db['Login_User']

                user_data = collection.find_one({"Username":self.Username_Entry.get()})

                if user_data:

                    if user_data["New Password"] == self.Password_Entry.get():
                        messagebox.showinfo("Success","Login Successful",parent = self.mw)
                        self.mw.destroy()
                        welcome_app = Welcome_Page()
                        welcome_app.mw.mainloop()
                        print(" Opening welcome Page")
                    else:
                        messagebox.showwarning("Wrong Password", "Please check the Password",parent=self.mw)
                else:
                    messagebox.showwarning("Wrong Username!!" ,"Please Enter the correct Username", parent=self.mw )

            except Exception as es:
                messagebox.showinfo('Wrong Username or Password!!!',parent=self.mw)
                
    def Newuser(self):
        self.mw.destroy()
        new_user_app = New_User()
        new_user_app.mw.mainloop()
             
class Welcome_Page:
    def __init__(self):
        self.mw = tk.Tk() #Create the main window
        self.mw.iconphoto(True,tk.PhotoImage(file = "S.png"))  #Set the window icon
        self.mw.title("Salary Prediction")  #Set the Title Name
        self.mw.geometry("300x230") #Set the windows size
        self.mw.configure(bg = "skyblue") #Set the window background color
        
        self.value = 0  #default value 

        #Create three frames to Organize the UI elements
        self.top_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.top_frame.pack()

        self.mid_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.mid_frame.pack()

        self.bottom_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.bottom_frame.pack()

        #Image on the page 
        img = Image.open("Login_Page_Img.png")
        img = ImageTk.PhotoImage(img)
        self.Login_Image = tk.Label(self.top_frame, image = img, bg = "skyblue")
        self.Login_Image.image = img
        self.Login_Image.pack()
        
        #Label and text in welcome page
        self.display_frame = tk.Label(self.mid_frame, text = "Welcome Mr/Ms Bhavnik", bg = "skyblue", foreground="Red")
        self.display_frame.pack()
        
        #Label and text in welcome page    
        self.display1_frame = tk.Label(self.mid_frame, text = "to the Salary Prediction Center",bg = "skyblue", foreground="Red")
        self.display1_frame.pack()

        #Label and text in welcome page
        self.display2_frame = tk.Label(self.mid_frame, text = "Click the Below Button for Prediction",bg = "skyblue", foreground="Red")
        self.display2_frame.pack()

        #Login, Forgot and New Registration Button 
        self.Salary_Prediction_Button = tk.Button(self.bottom_frame,text = "Salary Prediction", bg = 'light Blue',command = self.Rate)
        self.Salary_Prediction_Button.pack(side = "left", padx = 4,pady = 5)

        #Login, Forgot and New Registration Button 
        self.Decision_Tree_Button = tk.Button(self.bottom_frame,text = "Decision Tree", bg = 'light green', command = self.Dectree)
        self.Decision_Tree_Button.pack(side = "left", padx = 4,pady = 5)
        
         #Login, Forgot and New Registration Button 
        self.Back_Button = tk.Button(self.top_frame,text = "Back", bg = 'light green', command = self.Back)
        self.Back_Button.pack()
        
        tk.mainloop()
    
    #Method for passing commnad to Back Button
    def Back(self):
        self.mw.destroy()
        new_back_app = Login()
        new_back_app.mw.mainloop()
    
    #Method for passing commnad to Decision tree    
    def Dectree2(self):
        img_window = tk.Toplevel(self.mw)
        img_window.title('Decision Tree Image')
        decision_tree_image = Image.open('salarydecisiontree.png')
        photo = ImageTk.PhotoImage(decision_tree_image)

        self.Image = tk.Label(img_window, image = photo)
        self.Image.image = photo
        self.Image.pack()
        
    #Method for passing commnad to Prediction
    def Rate(self):
        self.mw.destroy()
        new_rate_app=RatingPredictionApp()
        new_rate_app.mw.mainloop()
    
    #Method for passing commnad to Back Decision tree    
    def Dectree(self):
        #Connect to your MongoDB and fetch the data
        client = MongoClient("mongodb://localhost:27017/")
        db = client['Salary_Prediction']
        collection = db['Glassdoor_jobs']
        data = list(collection.find({}, {"Founded" :1, "Rating":1}))

        #Create a DataFrame from the MongoDB data
        data2 = pd.DataFrame(data)
        """S = {'501 to 1000 employees':5, '10000+ employees':8, '1001 to 5000 employees':6,
        '51 to 200 employees':3, '201 to 500 employees':4, '5001 to 10000 employees':7,
        '1 to 50 employees':2, 'Unknown':0, '-1':1}"""

        #data2["Size"] = data2['Size'].map(S)
        #Predict "Rating" based on "Founded" column
        X = data2[["Founded"]]
        y = data2["Rating"]

        #Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

        #Create ad train a decision tree model
        model = DecisionTreeRegressor()
        model.fit(X_train, y_train)

        #make prediction on the test set
        y_pred = model.predict(X_test)

        #evalutate the model
        mse = mean_squared_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)

        print("Mean Square Error:",mse)
        print("R-squared:", r2)

        #Create a decision tree 
        data = export_graphviz(model,out_file = None,filled = True, rounded = True, special_characters = True, impurity = False, proportion = True, precision=2)
        graph = pydotplus.graph_from_dot_data(data)
        graph.write_png("salarydecisiontree.png")

        #show displays the decision tree graphics
        plt.imshow(plt.imread("salarydecisiontree.png"))
        plt.axis("off")
        plt.show()
        #self.mw.destroy()

#New class with GUI and to add new user in database
class New_User:
    def __init__(self):
        self.mw = tk.Tk() #Create the main window
        self.mw.iconphoto(True,tk.PhotoImage(file ="S.png"))  #Set the window icon
        self.mw.title("New User Registration")  #Set the Title Name
        self.mw.geometry("600x300") #Set the windows size
        self.mw.configure(bg = "skyblue") #Set the window background color
        
        self.value = 0  #default value 
        
        #Create a Frame in GUI using grid 
        self.top_frame = tk.Frame(self.mw, bg = 'Skyblue')
        self.top_frame.grid(row = 0,column = 0,sticky = "nsew")

        #Create a Frame in GUI using grid 
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
        self.Back_Button = tk.Button(self.top_frame, text = "Back", bg = 'light green', command = self.Back)
        self.Back_Button.grid(row=0, column=0, padx=4, pady=4,sticky = 'ne')
        
        tk.mainloop()
    
    #Method for passing commnad to login page     
    def Back(self):
        self.mw.destroy()
        new_back_app = Login()
        new_back_app.mw.mainloop()
    #Method for passing all the data to mongodb and storing it    
    def output(self):
        
        client = MongoClient("mongodb://localhost:27017/")
        db = client['Salary_Prediction']
        collection = db['Login_User']
        
        #Printing all the entry on the GUI
        print(self.Username_Entry.get())
        print(self.First_Name_Entry.get())
        print(self.Middle_Name_Entry.get())
        print(self.Last_Name_Entry.get())
        print(self.Date_of_Birth_Entry.get())
        print(self.New_Password_Entry.get())
        print(self.Confirm_New_Password_Entry.get())
        
        #Getting the entry from the Gui 
        username = self.Username_Entry.get()
        first_name = self.First_Name_Entry.get()
        middle_name = self.Middle_Name_Entry.get()
        last_name = self.Last_Name_Entry.get()
        Date_of_Birth = self.Date_of_Birth_Entry.get()
        new_password = self.New_Password_Entry.get()
        confirm_password = self.Confirm_New_Password_Entry.get()
        
        #Condition passed to check if the entry is empty or not
        if not(username and first_name and middle_name and last_name and Date_of_Birth and new_password and confirm_password):
            messagebox.showwarning(" Please fill all the required details")
            
        #to check if the password matches or not
        elif new_password == confirm_password or "":
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

#Class for Predicting the rating
class RatingPredictionApp:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title('Rating Prediction')
        self.mw.iconphoto(True,tk.PhotoImage(file = "S.png"))  #Set the window icon
        self.mw.geometry('400x400')
        self.mw.configure(bg = 'skyblue')
        
        #GUI window frame and its devision on the top frame
        self.top_frame = tk.Frame(self.mw,bg = 'skyblue')
        self.top_frame.grid(row=0,column=0,sticky="nsew")
        
        #GUI window frame for middle frame
        self.mid_frame = tk.Frame(self.mw,bg = 'skyblue')
        self.mid_frame.grid(row=1,column=0,sticky="nsew")

        #GUI window frame for middle left frame
        self.mid_left_frame = tk.Frame(self.mid_frame, bg = 'skyblue')
        self.mid_left_frame.grid(row = 0, column= 0, sticky = "nsew")
        
        #GUI window frame for middle right frame
        self.mid_right_frame = tk.Frame(self.mid_frame, bg = 'skyblue')
        self.mid_right_frame.grid(row = 0, column= 1, sticky = "nsew")
        
        #Label as Header
        self.Header_text = tk.Label(self.top_frame, bg = "skyblue",text = "Salary Prediction", font = ("Times New Roman",20,"bold"))
        self.Header_text.grid(padx = 95,pady = 10,sticky = "ne")
        
        #Image on the page 
        img = Image.open("Salary.png")
        img = ImageTk.PhotoImage(img)
        self.Login_Image = tk.Label(self.mid_left_frame, image = img, bg = "skyblue")
        self.Login_Image.image = img
        self.Login_Image.grid(row = 3, column = 0, padx = 5)
        
        #Calling the database from Mongodb
        client = MongoClient("mongodb://localhost:27017/")
        db = client['Salary_Prediction']
        collection = db['Glassdoor_jobs']

        data = list(collection.find())
        data2 = pd.DataFrame(data)

        # Function to perform the prediction
        def predict_rating():
            founded_value = float(founded_entry.get())
            rating_pred = model.predict([[founded_value]])[0]
            result_label.config(text=f'Predicted Rating: {rating_pred:.2f}')

        # Split the data into training and testing sets
        X = data2[['Founded']]
        y = data2['Rating']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Create a label and input field for 'Founded'
        founded_label = tk.Label(self.mid_right_frame, text='Founded:',font=12, bg = 'skyblue')
        founded_label.grid(row = 4, column=0, padx = 4, pady = 4)
        founded_entry = tk.Entry(self.mid_right_frame, bg= 'light blue')
        founded_entry.grid(row = 6,column = 0,pady = 4)

        # Create a button to predict the 'Rating'
        predict_button = tk.Button(self.mid_right_frame, text='Predict Rating',bg = "light green", command=predict_rating)
        predict_button.grid(row = 7,column = 0, pady = 4)

        # Create a label to display the prediction result
        result_label = tk.Label(self.mid_right_frame, bg = 'skyblue',text='')
        result_label.grid(row = 8, column = 0, pady = 4)
        
        #Login, Forgot and New Registration Button 
        self.Back_Button = tk.Button(self.mid_right_frame,text = "Back to welcome", bg = 'light green', command = self.Back_to)
        self.Back_Button.grid(row = 10, column = 0, pady = 4)

        self.mw.mainloop()
    
    #Method for command to go back to welcome page
    def Back_to(self):
        self.mw.destroy()
        new_back_to_app = Welcome_Page()
        new_back_to_app.mw.mainloop()
    
if __name__ == '__main__':
    app = Login()
    app.mw.mainloop



