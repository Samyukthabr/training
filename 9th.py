# Take input from user for the list of numbers
num_list = input("Enter a list of numbers: ")

# Split the input string into a list of numbers
num_list = list(map(int, num_list.split()))

# Initialize an empty list to store the squared numbers
squared_list = []

for num in num_list:
    # Square the number and append it to the squared_list
    squared_list.append(num ** 2)

# Print the list of squared numbers
print("List of squared numbers:", squared_list)
