"""Program asking difficulty Level - v1
ask what level of difficulty does the user want to play, Easy(1) or Hard(2)
Created by Elme Pieterse
04/05/2023
"""
# Ask what level difficulty
difficulty = int(input("What level of difficulty do you want to choose:\n"
                       "If you want the easy level type the number '1'\n"
                       "or, '2' if you want the hard level: "))

# If user inputs '1' output the easy level questions
if difficulty == 1:
    print("Easy level questions")

# If user inputs '2' output the hard level questions
elif difficulty == 2:
    print("Hard level questions")

# Otherwise display required inputs
else:
    print("Please enter the numerals '1' or '2': ")
