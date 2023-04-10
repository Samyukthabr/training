
# create a new list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(squares) 



# create a new list of even numbers from an existing list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 69, 10]
evens = [i for i in numbers if i % 2 == 0]
print(evens)


# create a new list of strings, where each string is the original string capitalized
words = ['apple', 'banana', 'cherry', 'date']
capitalized = [word.capitalize() for word in words]
print(capitalized) 

