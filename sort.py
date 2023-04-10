names = input("Enter a list of names, separated by spaces: ")
name_list = names.split()

sorted_names = sorted(name_list)


for name in sorted_names:
    print("sorted list:",name)
