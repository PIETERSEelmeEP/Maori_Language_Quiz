"""Program asking difficulty Level - v2
This converts the program form 02_Difficulty_Level_1_2_v1 into a loop
inorder to make it easier and more effective to test
Created by Elme Pieterse
05/05/2023
"""

difficulty = ""
while difficulty != 'x':

    # Ask what level difficulty
    difficulty = int(input("What level of difficulty do you want to choose: "
                           "Easy(1) or Hard(2): "))

    # If user inputs '1' output the easy level questions
    if difficulty == 1:
        print("Easy level questions")

    # If user inputs '2' output the hard level questions
    elif difficulty == 2:
        print("Hard level questions")

    # Otherwise display required inputs
    else:
        print("Please enter the numerals '1' or '2'")

    print(f"You entered Level {difficulty}")
