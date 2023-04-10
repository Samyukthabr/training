numbers = input("Enter a list of numbers").split(",")
number_list = [float(num.strip()) for num in numbers]

largest = max(number_list)
smallest = min(number_list)

print("Largest number:", largest)
print("Smallest number:", smallest)
