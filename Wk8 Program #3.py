#Reilly Kurth
#3/18/2025

states_capitals = {"Minnesota": "St. Paul", "Iowa": "Des Moines","Wisconsin": "Madison","South Dakota": "Pierre","North Dakota": "Bismarck", "Nebraska": "Lincoln","Illinois": "Springfield", "Texas": "Austin"}

def capital_quiz():
    correct = 0
    incorrect = 0

    for state in states_capitals:
        capital_guess = input(f"What is the capital of {state}? ").strip()

        if capital_guess.lower() == states_capitals[state].lower():
            print("correct")
            correct += 1
        else:
            print("incorrect")
            incorrect += 1

    print("Quiz Complete!")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

capital_quiz()