def get_age():
    age = input("[->] Enter your age: ")
    return age

def get_gender():
    while True:
        gender = input("[->] Enter your gender (m/f): ")
        
        if gender == "m":
            return "Male"
        elif gender == "f":
            return "Female"
        else:
            print("[!] Invalid input, please type either 'm' for male or 'f' for female.")
            

def smoking():
    while True:
        smoking = input("[->] Do you smoke at least once per week? (y/n): ")
        
        if smoking == "y":
            return "Yes"
        elif smoking == "n":
            return "No"
        else:
            print("[!] Invalid input, please type either 'y' for yes or 'n' for no.")


def risk():
    while True:
        risk = input("[->] Does any of your alive or dead relative have/had cancer before? (y/n): ")
        
        if risk == "y":
            return "Yes"
        elif risk == "n":
            return "No"
        else:
            print("[!] Invalid input, please type either 'y' for yes or 'n' for no.")

def workout():
    while True:
        workout = int(input("[->] How many hours do you workout per week on average? : "))
        
        if workout > 10:
            return 10
        else:
            return workout
        
def alcohol():
    while True:
        drinks = int(input("[->] What is the number of alcohol units consumed per week on average: "))
        
        if drinks > 5:
            return 5
        else:
            return drinks

def history():
    while True:
        history = input("[->] Have you ever had any form of cancer in the past? (y/n): ")
        
        if history == "y":
            return "Yes"
        elif history == "n":
            return "No"
        else:
            print("[!] Invalid input, please type either 'y' for yes or 'n' for no.")

def height():
    while True:
        height = float(input("[->] Enter your height in meters (etc 1.82): "))
        
        if height:
            return height
        else:
            print("[!] Please insert a value.")

def kilos():
    while True:
        weight = float(input("[->] Enter your weight in kilos (etc 72): "))
        
        if weight:
            return weight
        else:
            print("[!] Please insert a value.")