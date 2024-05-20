import os
from typing import List
from modules import functions

user_prompt: str
user_prompt = "Type add, show, edit, complete or exit: "
to_dos: List[str]
to_dos = functions.get_todos()

user_action: str

while True:
    user_action = input(user_prompt).strip().lower()
    
    if user_action.startswith("add") or user_action.startswith("new") or user_action.startswith("more"):
        user_todo = user_action[4:] or input("Enter a to-do: ")
        to_dos.append(user_todo)
        functions.write_todos(to_dos)
    elif user_action.startswith("show") or user_action.startswith("display"):
        if not to_dos:
            print("You have no to-dos.")
        else:
            for index, item in enumerate(to_dos):
                item = item.capitalize()
                row = f'{index + 1} - {item}'
                print(row)
    elif user_action.startswith("edit") or user_action.startswith("change") or user_action.startswith("modify"):
        if not to_dos:
            print("You have no to-dos.") 
        else: 
            try:
                edit_todo: str = user_action[5:] or input("Enter the number of the to-do you want to edit: ")
                to_edit: int = int(edit_todo)
                if to_edit > len(to_dos):
                    print("You are out of range.")
                else:
                    new_todo = input("Enter a new to-do: ")
                    to_dos[to_edit - 1] = new_todo
                    functions.write_todos(to_dos)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
    elif user_action.startswith("complete") or user_action.startswith("done") or user_action.startswith("finish")  or user_action.startswith("remove"):
            if not to_dos:
                print("You have no to-dos.") 
            else:               
                try:
                    completed_todo: str = user_action[9:] or input("Enter the number of the to-do you want to complete: ")
                    to_complete: int = int(completed_todo)
                    index: int = to_complete - 1
                    removed_task: str = to_dos[index] 
                    to_dos.pop(index)
                    functions.write_todos(to_dos)
                    message: str = f"{removed_task} has been removed." if to_dos else "You have no to-dos."
                    print(message)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                except IndexError:
                    print("Invalid input. Please enter a number within the range of number ot all items.")
                    continue
    elif user_action.startswith("exit") or user_action.startswith("quit") or user_action.startswith("stop") or user_action.startswith("end"):
        functions.write_todos(to_dos)
        break
    else:
        print("Invalid input")
    

print(f"You entered: {to_dos}")