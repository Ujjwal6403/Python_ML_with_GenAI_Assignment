import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1 : Load Dataset
data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Dataset is :")
print(data)

# Step 2 : Label Encoding
le_weather = LabelEncoder()
le_temp = LabelEncoder()
le_play = LabelEncoder()

data['Weather'] = le_weather.fit_transform(data['Weather'])
data['Temperature'] = le_temp.fit_transform(data['Temperature'])
data['Play'] = le_play.fit_transform(data['Play'])

print("\nEncoded Dataset :")
print(data)

# Features and Label
X = data[['Weather','Temperature']]
Y = data['Play']

# Step 3 : Train Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)

# Step 4 : Test Data
weather = input("Enter Weather (Sunny/Overcast/Rainy): ")
temp = input("Enter Temperature (Hot/Mild/Cold): ")

weather = le_weather.transform([weather])[0]
temp = le_temp.transform([temp])[0]

result = model.predict([[weather,temp]])

if result == 1:
    print("Play : Yes")
else:
    print("Play : No")

# Step 5 : Accuracy Function
def CheckAccuracy():

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(Y_test,pred)

    print("Accuracy is :",acc*100)
    
def main():
   
   CheckAccuracy()
if __name__ == "__main__":
   main()

CheckAccuracy()