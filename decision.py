import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.metrics import mean_squared_error, r2_score
import pydotplus

#importing csv file 
data2 = pd.read_csv("glassdoor_jobs.csv")

# We'll predict 'Rating' based on other columns
X = data2[['Founded']]
y = data2['Rating']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

data2 = export_graphviz(model, out_file = None, filled = True, rounded = True)
graph = pydotplus.graph_from_dot_data(data2)
graph.write_png("Mydecisiontree.png")
