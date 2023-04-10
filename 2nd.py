# take the input from the user
s = "Sushma"
vowels = "aeiouAEIOU"
new_string = ""

#check whether there is a vowel in the string
for char in s:
    if char not in vowels:
        new_string += char
        
#print the result
print(new_string)  
