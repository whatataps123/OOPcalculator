# Joshua Lemuel Z. Centina
# BS CpE 1-4
from userinterface import UserInterface
from calculator import Calculator
# Convert your previous calculator program into an OOP type of program.
ui = UserInterface()
calc = Calculator()
# pseudocode
# Ask user what operator will be used
operation = ui.user_choose()
# Insert handling errors
# Ask user for num1
num_1 = ui.input_num1()
# Insert handling errors
# Ask user num2
num_2 = ui.input_num2(operation)
# Insert handling errors
# Print the output
sum = calc.add(num_1,num_2)
# Ask the user again if they want to try again (y/n)
# Insert handling errors