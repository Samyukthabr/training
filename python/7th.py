# Take input from user for the list of numbers
num_list = input("Enter a list of numbers: ")

# Split the input string into a list of numbers
num_list = list(map(int, num_list.split()))

# Initialize an empty list to store the prime numbers
prime_list = []

# Iterate over each number in the list
for num in num_list:
    
    # Check if the number is greater than 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)

# Print the list of prime numbers
print("List of prime numbers:", prime_list)
