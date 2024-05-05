import os
from typing import List

user_prompt = "Type add, show, edit, complete or exit: "
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
    
    if "add" in user_action:
        user_todo = user_action[4:]
        to_dos.append(user_todo)
        with open(to_dos_file, "a") as file:   
            file.write(user_todo + "\n")
    elif "show" in user_action:
        if not to_dos:
            print("You have no to-dos.")
        else:
            for index, item in enumerate(to_dos):
                item = item.capitalize()
                row = f'{index + 1} - {item}'
                print(row)
    elif "edit" in user_action:
        if not to_dos:
            print("You have no to-dos.") 
        else: 
            try:             
                to_edit = int(user_action[5:])
                if to_edit > len(to_dos):
                    print("You are out of range.")
                else:
                    new_todo = input("Enter a new to-do: ")
                    to_dos[to_edit - 1] = new_todo
                    with open(to_dos_file, "w") as file:
                        for item in to_dos:
                            file.write(item + "\n")
            except ValueError:
                print("Invalid input")
    elif "complete" in user_action:
            if not to_dos:
                print("You have no to-dos.") 
            else:               
                to_complete = int(user_action[9:])
                if to_complete > len(to_dos):
                    print("You are out of range.")
                else:
                    try:
                        index = to_complete - 1
                        removed_task = to_dos[index] 
                        print(f"{removed_task} has been removed.")
                        to_dos.pop(index)
                        with open(to_dos_file, "w") as file:
                            for item in to_dos:
                                file.write(item + "\n")
                        message = "You have no to-dos." if not to_dos else f"{removed_task} has been removed."
                        print(message)
                    except ValueError:
                        print("Invalid input")
    elif "exit" in user_action:
        with open(to_dos_file, "w") as file:
            for item in to_dos:
                file.write(item + "\n")
        break
    else:
        print("Invalid input")
    

print(f"You entered: {to_dos}")