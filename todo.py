import os
# Set the name of the file to store the to-do list
filename = "todo.txt"

# Define a function to read the current to-do list
def read_todo_list():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return []

# Define a function to write the to-do list to the file
def write_todo_list(todo_list):
    with open(filename, "w") as f:
        f.write("\n".append(todo_list))

# Define a function to create a new to-do list item
def create_todo():
    todo = input("Enter a new to-do list item: ")
    todo_list = read_todo_list()
    todo_list.append(todo)
    write_todo_list(todo_list)
    print(f"{todo} has been added to your to-do list.")

# Define a function to read the current to-do list
def read_todo():
    todo_list = read_todo_list()
    if todo_list:
        print("Your to-do list:")
        for i, todo in enumerate(todo_list):
            print(f"{i+1}. {todo}")
    else:
        print("Your to-do list is empty.")

# Define a function to update a to-do list item
def update_todo():
    todo_list = read_todo_list()
    if todo_list:
        index = int(input("Enter the index of the item you want to update: "))
        if index > 0 and index <= len(todo_list):
            todo = input(f"Enter the new value for item {index}: ")
            todo_list[index-1] = todo
            write_todo_list(todo_list)
            print(f"Item {index} has been updated to {todo}.")
        else:
            print("Invalid index.")
    else:
        print("Your to-do list is empty.")

# Define a function to delete a to-do list item
def delete_todo():
    todo_list = read_todo_list()
    if todo_list:
        index = int(input("Enter the index of the item you want to delete: "))
        if index > 0 and index <= len(todo_list):
            todo = todo_list.pop(index-1)
            write_todo_list(todo_list)
            print(f"{todo} has been deleted from your to-do list.")
        else:
            print("Invalid index.")
    else:
        print("Your to-do list is empty.")

# Define a function to display the menu of options
def display_menu():
    print("Select an option:")
    print("1. Create a new to-do list item")
    print("2. Read your to-do list")
    print("3. Update a to-do list item")
    print("4. Delete a to-do list item")
    print("5. Exit")

# Define the main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            create_todo()
        elif choice == "2":
            read_todo()
        elif choice == "3":
            update_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
