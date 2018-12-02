questionDictionary = {
    1: "A person's age",
    2: "The name of a car model",
    3: "Grams in a kilogram",
}

answerDictionary = {
    "age": 3, "personAge": 3, "person_age": 3, "Person_Age": 2, "Age": 2, "person_Age": 2, "AGE": 1,
    "car_model": 3, "carModel": 3, "model": 2, "Car_model": 2, "CarModel": 2,
    "GRAMS_IN_KILOGRAM": 3,"GRAMS_IN_A_KILOGRAM": 3, "grams_in_kilogram": 2,"grams_in_a_kilogram": 2
}

def explanation(score):
    if score == 3:
        print("Noice, that was a spot on variable name")
    elif score == 2:
        print("The variable name you typed is acceptable but not quite right")
        print("Remember, variable names should be lowercase for regular variables and upper case for global constants")
        print("Variable names must also be concise to prevent any confusion down the line")
def mainActivity():
    score = 0
    for i in range(1,4):
        print("\n"+questionDictionary[i])
        userInput = input("Enter a suitable variable name: ")
        try:
            currentScore = answerDictionary[userInput]
        except:
            currentScore = 1
            print(currentScore)
        explanation(currentScore)
        score += currentScore
    print(score)
    return score

print("Welcome to the Variable Naming Convention Game or VNM for short")
print("Please enter a suitable variable name for each scenario")
begin = input("Begin Game(Y/N): ")
while begin != "Y" and begin != "N":
    begin = input("Begin Game(Y/N): ")
if begin == "Y":
    score = mainActivity()
    print("This is the end of the VNC game, your final score is ", score, "out of 9")
else:
    print("Nice")




