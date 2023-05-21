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
        
    