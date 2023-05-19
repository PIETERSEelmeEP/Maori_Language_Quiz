"""Program's play again function - v1
ask if user wants end the quiz of repeat
Created by Elme Pieterse
19/05/2023
"""
# Ask if user wants to end or restart the program
end_program = input("Do you want to exit the quiz? (Yes/No: ")
thanks_note = "thank you"

# If user inputs 'yes' output the thanks note
if end_program == "yes":
    print(thanks_note)

# If user inputs 'no' output 'Program restarts'
elif end_program == "no":
    print("Program restarts")

# Otherwise display required inputs
else:
    print("Please enter either 'Yes' or 'No': ")



