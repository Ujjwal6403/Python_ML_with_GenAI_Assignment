import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1 : Load dataset
data = pd.read_csv("MarvellousAdvertising.csv")

print("Dataset is :")
print(data.head())

# Step 2 : Prepare data
X = data[['TV','Radio','Newspaper']]
Y = data['Sales']

# Step 3 : Train dataset
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)

model = LinearRegression()

model.fit(X_train,Y_train)

print("Training completed")

# Step 4 : Test dataset
Y_pred = model.predict(X_test)

# Step 5 : Display predicted and expected values
result = pd.DataFrame({
    "Expected":Y_test,
    "Predicted":Y_pred
})

print("Expected vs Predicted values")
print(result)