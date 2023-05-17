"""Program calculates the users points - v1
This will calculate the/add/subtract points according to the result_answer,
already put into a function of sum sort/planning
Created by Elme Pieterse
16/05/2023
"""


def calculate_points_show_results():
    points = 0

    result_answer = "correct" or "incorrect"

    if result_answer == "correct":
        points += 10
        print(points)
    else:
        points -= 5
        print(points)


# Main Routine
calculate_points_show_results()
