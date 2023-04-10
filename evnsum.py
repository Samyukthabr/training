numbers = input("Enter a list of numbers").split(",")
number_list = [int(num) for num in numbers]

even_sum = 0

for num in number_list:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)
