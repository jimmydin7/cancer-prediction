import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('cancer_db.csv')

#spliting
#X contains all values for each line except from diagnosis
X = df.drop('Diagnosis', axis=1)

#y contains diagnosis for each line (1 = true, 0 = false)
Y = df['Diagnosis']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#train the model

model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)

def predict(patient_dataframe):
     cancer_prediction = model.predict(patient_dataframe)

     if cancer_prediction[0] == 1:
          probability = model.predict_proba(patient_dataframe)[0][1] * 100
          return probability
     else:
          return None
     
