"""Program calculates the users points - v1
This will calculate the/add/subtract points according to the result_answer,
already put into a function of sum sort/planning
Created by Elme Pieterse
16/05/2023
"""


def calculate_points():
    points = STARTING_POINTS
    for item in range(10):
        result_answer = ""  # the question and answer function will go here
        if result_answer == "correct":
            points += 10
            print(f"you have {points} points")
        else:
            points -= 5
            print(f"you have {points} points")


# Main Routine
STARTING_POINTS = 0
calculate_points()
