

# Define a function to display the menu of options
def display_menu():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

# Define the main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "6":
            break
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == "1":
                result = num1+num2
            elif choice == "2":
                result = num1-num2
            elif choice == "3":
                result = num1*num2
            elif choice == "4":
                result = num1/num2
            elif choice=="5":
                result = num1%num2
            else:
                print("Invalid choice. Try again.")
                continue
            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Try again.")
        except ZeroDivisionError:
            print("Cannot divide by zero")

if __name__ == "__main__":
    main()
