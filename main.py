import os
from typing import List

user_prompt = "Type add, show, edit, complete or exit: "
user_edit = "Type the number of to-do item you want to edit: "
script_dir = os.path.dirname(__file__)
to_dos_file = os.path.join(script_dir, "to_dos.txt")
to_dos: List[str]

if not os.path.exists(to_dos_file):
    to_dos = []
    file = open(to_dos_file, "w")
    file.close()
else:
    print("File exists")
    print(os.path.abspath(to_dos_file))
    with open(to_dos_file, "r") as file:
        to_dos = file.readlines()
        to_dos = [item.strip() for item in to_dos]

while True:
    user_action = input(user_prompt).strip().lower()
    match user_action:
        case "add":
            user_todo = input("Enter a to-do: ")
            to_dos.append(user_todo)
            with open(to_dos_file, "a") as file:   
                file.write(user_todo + "\n")
        case "show":
            if not to_dos:
                print("You have no to-dos.")
            else:
                for index, item in enumerate(to_dos):
                    item = item.capitalize()
                    row = f'{index + 1} - {item}'
                    print(row)
        case "edit":
            to_edit = int(input(user_edit))
            if to_edit > len(to_dos):
                print("You are out of range.")
            else:
                new_todo = input("Enter a new to-do: ")
                to_dos[to_edit - 1] = new_todo
        case "complete":
            try:
                to_complete = int(input("Enter the number of to-do item you want to complete: "))
                if to_complete > len(to_dos):
                    print("You are out of range.")
                else:
                    to_dos.pop(to_complete - 1)
                    with open(to_dos_file, "w") as file:
                        for item in to_dos:
                            file.write(item + "\n")
            except ValueError:
                print("Invalid input")
        case "exit":
            with open(to_dos_file, "w") as file:
                for item in to_dos:
                    file.write(item + "\n")
            break
        case whatever:
            print("Invalid input")
    

print(f"You entered: {to_dos}")