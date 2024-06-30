def announce(age, gender, smoking, risk, workout, drinks, history):
    if smoking == 'Yes':
        sentence_smoking = "You smoke at least once per week."
    else:
        sentence_smoking = "You do not smoke."

    if risk == 'Yes':
        sentence_risk = "You have some family cancer past."
    else:
        sentence_risk = "You do not have any family cancer past."

    if workout >= 10:
        sentence_workout = "You workout 10 or more hours per week."
    else:
        sentence_workout = f"You workout {workout} hours per week."

    if drinks >= 5:
        sentence_drinks = "You consume 5 or more alcoholic units per week."
    else:
        sentence_drinks = f"You consume {drinks} alcoholic units per week."

    if history == 'Yes':
        sentence_history = "You have had cancer in the past."
    else:
        sentence_history = "You have never had cancer in the past."

    print(f"""
-------------------------------------
You are {age} years old.
You are a {gender}
{sentence_smoking}
{sentence_risk}
{sentence_workout}
{sentence_drinks}
{sentence_history}

Starting BMI prediction...
-------------------------------------
""")
