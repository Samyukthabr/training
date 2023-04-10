while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        if denominator <= 0:
            raise ValueError("Denominator must be positive and non-zero.")
        if numerator <= denominator:
            raise ValueError("Numerator must be greater than denominator.")
        result = numerator / denominator
        break
    except ValueError as error:
        print(f"Error: {error}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
print(f"{numerator} / {denominator} = {result}")
