import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('cancer_db.csv')

# Spliting

#X contains all values for each line except from diagnosis
X = df.drop('Diagnosis', axis=1)

#Y contains just the diagnosis for each line (1 = true, 0 = false)
y = df['Diagnosis']


#Split the data into training and testing sets. Training is 20% because of 0.2
# Putting random state 42 so we have the same result each time for same patient
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


def predict(patient):
    cancer_prediction = model.predict(patient)
    
    if cancer_prediction[0] == 1:
        probability = model.predict_proba(patient)[0][1] * 100
        return f"[!] Chance that patient has or might develop cancer in the future: {probability:.2f}%"
    else:
        return f"[-] Patient clear, no cancer!"
