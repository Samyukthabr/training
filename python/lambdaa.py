# Take user input for list of numbers
num_list = input("Enter a list of numbers, separated by commas: ").split(",")

# Use lambda function and list comprehension to filter out even numbers and double odd numbers
result_list = [(lambda x: x*2)(int(num)) for num in num_list if int(num)%2!=0]

# Print the resulting list
print(result_list)
