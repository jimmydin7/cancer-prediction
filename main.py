import pandas
from utils import bmi, fetch, formatter, machine_learning




if __name__ == '__main__':
    age = fetch.get_age()
    gender = fetch.get_gender()
    smoking = fetch.smoking()
    risk = fetch.risk()
    workout = fetch.workout()
    drinks = fetch.alcohol()
    history = fetch.history()
    height = fetch.height()
    weight = fetch.kilos()

    bmi = bmi.calculate_bmi(height=height, weight=weight)
    
    if gender == 'Male':
        new_gender = 0
    else:
        new_gender = 1

    if smoking == 'Yes':
        new_smoking = 1
    else:
        new_smoking = 0

    if risk == 'Yes':
        new_risk = 1
    else:
        new_risk = 0

    if history == 'Yes':
        new_history = 1
    else:
        new_history = 0


    patient = pandas.DataFrame({
        'Age': [age],
        'Gender': [new_gender],
        'BMI': [int(bmi)],
        'Smoking': [new_smoking],
        'GeneticRisk': [new_risk],
        'PhysicalActivity': [workout],
        'AlcoholIntake': [drinks],
        'CancerHistory': [new_history]
    })
    
    print("-------------------------------------")
    print("Generated Dataframe")
    print("-------------------------------------")
    print(patient)
    formatter.announce(age, gender, smoking, risk, workout, drinks, history)
    
    print(f"""
Successfully calculated BMI! -> {bmi}

Starting cancer prediction...
-------------------------------------
""")
    print(machine_learning.predict(patient))
    