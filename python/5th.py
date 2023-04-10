# Take input from user for the first list
list1 = input("Enter the first list of numbers (separated by spaces): ")

# Split the input string into a list of numbers
list1 = list(map(int, list1.split()))

# Take input from user for the second list
list2 = input("Enter the second list of numbers (separated by spaces): ")

# Split the input string into a list of numbers
list2 = list(map(int, list2.split()))

# Create an empty list to store the common elements
common_elements = []

# Iterate over each element in list1
for num in list1:
    
    # If the element is also in list2 and not already in common_elements list
    if num in list2 and num not in common_elements:
        
        # Add the element to the common_elements list
        common_elements.append(num)

# Print the common elements
print("Common elements in both lists:", common_elements)
