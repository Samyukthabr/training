input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_str.split()]

numbers_sorted = sorted(numbers)

length = len(numbers_sorted)

if length % 2 == 0:

    median = (numbers_sorted[length//2 - 1] + numbers_sorted[length//2]) / 2
else:
    
    median = numbers_sorted[length//2]
print("The median value of the list is:", median)
