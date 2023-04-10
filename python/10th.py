# Get a list of strings from the user
input_list = input("Enter a list of strings").split(",")

# Create an empty list to hold the palindromes
palindrome_list = []

# Loop through the input list and check if each string is a palindrome
for string in input_list:
    if string == string[::-1]:
        palindrome_list.append(string)

# Print the palindrome list
print("The palindromes in the input list are:", palindrome_list)
