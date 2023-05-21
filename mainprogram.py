# Joshua Lemuel Z. Centina
# BS CpE 1-4
from userinterface import UserInterface
# Convert your previous calculator program into an OOP type of program.
ui = UserInterface()
operation = ui.user_choose()
# pseudocode
# Ask user what operator will be used
ui.user_choose()
# Insert handling errors
# Ask user for num1
ui.input_num1()
# Insert handling errors
# Ask user num2
ui.input_num2(operation)
# Insert handling errors
# Print the output
# Ask the user again if they want to try again (y/n)
# Insert handling errors