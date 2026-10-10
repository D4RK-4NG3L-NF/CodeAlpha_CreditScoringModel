import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Load the data
df = pd.read_csv("credit_data.csv")
# Select input feature
X = df[["income", "debt", "payment_history", "credit_history_years"]]
# Select the target
Y = df["creditworthy"]
print("Dataset loaded Successfully!")
print("Feature:", X.shape)
print("Target:", Y.shape)
#create the model
model = LogisticRegression()
#Train the model using all five sample customer 
model.fit(X, Y)
print("Model trainned Successfully!")
#check prediction on the training set
training_predictions = model.predict(X)
#Calculate the training accuracy 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y, training_predictions)
print("Training accuracy:", accuracy)
print("Training accuracy percentage:", accuracy * 100 , "%")
# create sample new customer
new_custome = pd.DataFrame(
    [[60000, 12000, 1, 4]],
    columns=["income", "debt", "payment_history", "credit_history_years"]
)
#predict creditworthness
prediction = model.predict(new_custome)
if prediction[0] == 1:
    print("prediction: creditworthy")
else:
    print("prediction: Not creditwrothy")
