import tkinter as tk
from turtle import width
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.metrics import mean_squared_error,r2_score
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pydotplus

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

        self.display_frame = tk.Label(self.mid_frame, text = "Welcome Mr/Ms Bhavnik", bg = "skyblue", foreground="Red")
        self.display_frame.pack()

        self.display1_frame = tk.Label(self.mid_frame, text = "to the Salary Prediction Center",bg = "skyblue", foreground="Red")
        self.display1_frame.pack()

        self.display2_frame = tk.Label(self.mid_frame, text = "Click the Below Button for Prediction",bg = "skyblue", foreground="Red")
        self.display2_frame.pack()

        #Login, Forgot and New Registration Button 
        self.Salary_Prediction_Button = tk.Button(self.bottom_frame,text = "Salary Prediction", bg = 'light Blue')
        self.Salary_Prediction_Button.pack(side = "left", padx = 4,pady = 5)

        #Login, Forgot and New Registration Button 
        self.Decision_Tree_Button = tk.Button(self.bottom_frame,text = "Decision Tree", bg = 'light green',command = self.Dectree2)
        self.Decision_Tree_Button.pack(side = "left", padx = 4,pady = 5)
        
        tk.mainloop()
    def Dectree2(self):
        img_window = tk.Toplevel(self.mw)
        img_window.title('Decision Tree Image')
        decision_tree_image = Image.open('salarydecisiontree.png')
        photo = ImageTk.PhotoImage(decision_tree_image)

        self.Image = tk.Label(img_window, image = photo)
        self.Image.image = photo
        self.Image.pack()

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

        plt.imshow(plt.imread("salarydecisiontree.png"))
        plt.axis("off")
        plt.show()
        self.mw.destroy()

Welcome_Page()