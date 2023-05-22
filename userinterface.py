class UserInterface:
    def user_choose(self):
        print("Choose your desired operation:")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        while True:
            try:
                calc_operation = int(input("\nEnter the number of your desired operation (1-4): "))
                if calc_operation < 1 or calc_operation > 4:
                    raise ValueError("Invalid operation")
                break
            except ValueError:
                print("\033[1;31m" + "Invalid input for the operation. Please enter a number from 1 to 4. Try again." + "\033[1;m")
                
        return calc_operation
        
    def input_num1(self):
        while True:
            try:
                num_1 = float(input("\nEnter the first number: "))
                break
            except ValueError:
                print("\033[1;31m" + "Invalid input for the first number. Try again." + "\033[1;m")
        return num_1
    
    def input_num2(self, calc_operation):
        while True:
            try:
                num_2 = float(input("Enter the second number: "))
                if calc_operation == 4 and num_2 == 0:
                    # Insert handling errors
                    raise ZeroDivisionError("\033[1;31m" + "Cannot divide by zero. Please choose another number." + "\033[1;m")
                break
            except ValueError:
                print("\033[1;31m" + "Invalid input for the second number. Try again." + "\033[1;m")
            except ZeroDivisionError as error:
                print(error)
        return num_2