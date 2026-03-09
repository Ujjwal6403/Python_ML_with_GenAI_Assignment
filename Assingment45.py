from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1 : Load dataset
wine = load_wine()

X = wine.data
Y = wine.target

print("Total records :",len(X))

# Step 2 : Split dataset
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)

# Step 3 : Train model
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train,Y_train)

print("Model trained successfully")

# Step 4 : Test model
Y_pred = model.predict(X_test)

# Step 5 : Accuracy
acc = accuracy_score(Y_test,Y_pred)

print("Accuracy of model :",acc*100)