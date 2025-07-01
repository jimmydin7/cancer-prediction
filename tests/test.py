try:
    from src.model import model
except Exception as e:
    print("Please run this from the main directory / and run:   python -m tests.test")
import pandas as pd

demo_dataframe = pd.DataFrame([{
    'Age': 68,
    'Gender': 1,
    'BMI': 38.78508355516642,
    'Smoking': 0,
    'GeneticRisk': 1,
    'PhysicalActivity': 1.0682099296399061,
    'AlcoholIntake': 2.6429210071872116,
    'CancerHistory': 1
}])

diagnosis = model.predict(demo_dataframe)
print("starting test on")
print(demo_dataframe)
if diagnosis == None:
    print("patient clear")
else:
    print("chance of cancer -> ", diagnosis) 