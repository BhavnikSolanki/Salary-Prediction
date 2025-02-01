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
        self.Decision_Tree_Button = tk.Button(self.bottom_frame,text = "Decision Tree", bg = 'light green')
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
