# Salary Prediction System

![Salary Prediction UML](Salary_Prediction_UML.png)

A complete **Salary Prediction** desktop application built as **Assessment-1**.  
It features a clean Tkinter GUI with user registration & login, a Machine Learning model (Decision Tree Regressor + Linear Regression) to predict salaries based on job data, MongoDB integration for user data, and visualization of the decision tree.

## ✨ Features

- **User Authentication**
  - Registration form (`New_User.py`)
  - Login page with username/password
- **Salary Prediction GUI**
  - Input job-related features
  - Predicts salary using **DecisionTreeRegressor** and **LinearRegression**
  - Model evaluation (MSE & R² score)
- **Welcome & Thank You Screens**
- **Data Flow Visualization**
  - MongoDB → Python pipeline
  - UML diagram & flowcharts
- **Decision Tree Visualization** (using `pydotplus` + Graphviz style)
- Cleaned Glassdoor Jobs dataset

## 🛠️ Technologies Used

- **Python**
- **GUI**: Tkinter + `tkcalendar` + Pillow (PIL)
- **Machine Learning**: scikit-learn (`DecisionTreeRegressor`, `LinearRegression`)
- **Data**: pandas, numpy, matplotlib
- **Database**: pymongo (MongoDB)
- **Visualization**: pydotplus, matplotlib
- **Others**: Glassdoor salary dataset

## 📋 Prerequisites

Before running the code, install the required packages:

```bash
pip install pandas tkcalendar Pillow scikit-learn pymongo matplotlib pydotplus
```
Additional requirements:

.  MongoDB running locally (or update connection string in the code)
.  Unzip Salary_Prediction_Dataset.zip if needed (contains original dataset)

🚀 How to Run

1. Clone the repository:
   ```
   Bashgit clone https://github.com/BhavnikSolanki/Salary-Prediction.git
    cd Salary-Prediction
2.  Run the Welcome Page (recommended entry point):
   ```Bash
    python "Login GUI/Salary Prediction/Welcome_Page.py"
  ```
Or directly run the full login + prediction interface:
```Bash
    python "Login GUI/Salary Prediction/Salary_Prediction_and_GUI.py"
```
3.  Use the GUI to:
.  Register a new user
.  Log in
.  Enter job details and get a salary prediction


Alternative scripts (depending on your testing needs):

Salary Prediction/Salary_Prediction.py
Registration GUI/New_User.py

📁 Project Structure (Key Files)
Salary-Prediction/
├── Login GUI/
│   └── Salary Prediction/
│       ├── Salary_Prediction_and_GUI.py   # Main login + prediction GUI
│       ├── Welcome_Page.py                # Landing page
│       ├── Thank_you.py
│       ├── glassdoor_jobs.csv
│       └── salarydecisiontree.png
├── Registration GUI/
│   ├── New_User.py
│   └── (GUI images)
├── Salary Prediction/
│   ├── Salary_Prediction.py
│   ├── decision_tree.py
│   ├── decision.py
│   ├── Salary_Prediction_Dataset.zip
│   └── (flowcharts & UML)
├── Salary_Prediction_Dataset.zip
├── Assessment 1(Salary Prediction).docx
├── Before running this code.txt
├── decision_tree.py
├── Flowchart_Mongodb_to_Python.png
├── Salary_Prediction_Flowchart .png
├── Salary_Prediction_UML.png
└── README.md

📊 Dataset

Source: Glassdoor job postings (glassdoor_jobs.csv)
Includes job title, experience, location, skills, etc.
Pre-cleaned versions also available (salary_data_cleaned.csv, eda_data.csv)

🤖 Model

Primary: DecisionTreeRegressor
Secondary: LinearRegression
Trained on the Glassdoor dataset
Visualized decision tree saved as PNG (salarydecisiontree.png, Mydecisiontree.png)

📸 Screenshots & Diagrams
Description,Image
System UML Diagram,"<img src=""Salary_Prediction_UML.png"" alt=""UML"">"
MongoDB → Python Flowchart,"<img src=""Flowchart_Mongodb_to_Python.png"" alt=""Flowchart"">"
Salary Prediction Flowchart,"<img src=""Salary_Prediction_Flowchart%20.png"" alt=""Flowchart"">"
Decision Tree Visualization,"<img src=""salarydecisiontree.png"" alt=""Decision Tree"">"
Planning Sketches,"<img src=""Planning1.jpg"" alt=""Planning"">"

📄 License
This project is for educational/assessment purposes. No license specified.

Made as part of Assessment-1
Feel free to fork, improve the GUI, add more models (Random Forest, XGBoost), or connect it to a proper backend!
Any questions or suggestions? Open an issue or reach out to the repo owner.

You can copy the entire content above and paste it into your **README.md** file.  
It will render beautifully on GitHub with proper formatting, images, and tables.  

Would you like any modifications (e.g., add badges, change tone, include performance metrics from the docx, or make it shorter)? Just let me know!
