# Joshua Lemuel Z. Centina
# BS CpE 1-4
import time
import sys
from userinterface import UserInterface
from calculator import Calculator
from childcalculator import ChildCalculator
# Convert your previous calculator program into an OOP type of program.
ui = UserInterface()
calc = Calculator()
child = ChildCalculator()

print("=============================================================================")
def typewriter(text, delay=0.1):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()
typewriter("\033[1;46m" + "Welcome to Joshua Lemuel Z. Centina's Calculator" + "\033[1;m")

print("\nLoading:")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

#Start
while True:
    operation = ui.user_choose()
    num_1 = ui.input_num1()
    num_2 = ui.input_num2(operation)
    if operation == 1:
        child.add()
        sum = calc.add(num_1,num_2)
        sqrtAdd = child.sqrtAdd(sum)
        child.add()
        print("The sum:", "\033[1;43m" + str(sum) + "\033[1;m")
        print("The square root is", sqrtAdd)

    elif operation == 2:
        diff = calc.subtract(num_1,num_2)
        sqrtSub = child.sqrtSub(diff)
        print("The difference:", "\033[1;43m" + str(diff) + "\033[1;m")
        print("The square root is", sqrtSub)

    elif operation == 3:
        product = calc.multiply(num_1,num_2)
        sqrtMult = child.sqrtMult(product)
        print("The product:", "\033[1;43m" + str(product) + "\033[1;m")
        print("The square root is:", sqrtMult)

    elif operation == 4:
        quotient = calc.divide(num_1,num_2)
        sqrtDiv = child.sqrtDiv(quotient)
        print("The quotient:", "\033[1;43m" + str(quotient) + "\033[1;m")
        print("The square root is:", sqrtDiv)

    if not ui.retry():
        break