import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor,export_graphviz
from sklearn.metrics import mean_squared_error,r2_score
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pydotplus

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