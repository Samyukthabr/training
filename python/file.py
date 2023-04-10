while True:
    try:
        filename = input("Enter a filename: ")
        with open(filename) as file:
            contents = file.read()
            print(contents)
        break
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please enter a valid filename.")
