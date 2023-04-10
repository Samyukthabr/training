# Take input from user for the string
input_str = input("Enter a string: ")

# Create an empty dictionary to store the count of each letter
letter_count = {}

for char in input_str:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1

# Print the count of each letter
for char, count in letter_count.items():
    print(f"{char}: {count}")
