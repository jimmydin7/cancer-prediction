# Cancer Prediction ML

A web app that predicts the probability of cancer based on user medical and lifestyle data, using a machine learning model (Random Forest) trained on a public dataset.

## View demo
- View live on [https://jimdin123.pythonanywhere.com](https://jimdin123.pythonanywhere.com/)
## Features
- friendly webUI with tailwindCSS for frontend and Flask for backend
- get data for age, gender, weight, height, smoking and alcohol habits, genetic risk, physical activity, and cancer history
- calculates BMI from weight and height
- predicts cancer risk probability using a trained Random Forest model

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/jimmydin7/cancer-prediction.git
cd cancer-prediction
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python main.py
```

4. **Open your browser**

Go to [http://localhost:5000](http://localhost:5000) and start the prediction!

## How it works
- the app asks you some questions about your health and lifestyle
- after submitting, it calculates your BMI and feeds all answers to a Random Forest model
- the model outputs your probability of having cancer

## Dataset
- the model is trained on a public dataset with the following columns:
  - Age, Gender, BMI, Smoking, GeneticRisk, PhysicalActivity, AlcoholIntake, CancerHistory, Diagnosis
- the model is retrained every time the app starts (for demo/educational purposes).

## Requirements
- Python 3.7+
- Flask
- pandas
- scikit-learn

## Credits
- created with love by jim to raise awareness for cancer using machine learning
- Dataset: [Kaggle public cancer dataset](https://www.kaggle.com/)

## Disclaimer
this project is for educational and awareness purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment.
