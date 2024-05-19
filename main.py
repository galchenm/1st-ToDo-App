import os
from typing import List

def get_todos(filename: str = "to_dos.txt") -> List[str]:
    """Reads the to-dos from a file and returns them as a list.

    Args:
        filename (str, optional): _description_. Defaults to "to_dos.txt".

    Returns:
        List[str]: _description_
    """
    script_dir = os.path.dirname(__file__)
    to_dos_file = os.path.join(script_dir, filename)
    to_dos_local: List[str]

    if not os.path.exists(to_dos_file):
        to_dos_local = []
        file = open(to_dos_file, "w")
        file.close()
    else:
        print("File exists")
        print(os.path.abspath(to_dos_file))
        with open(to_dos_file, "r") as file:
            to_dos_local = file.readlines()
            to_dos_local = [item.strip() for item in to_dos_local]
    return to_dos_local


def write_todos(to_dos_local: List[str], filename: str = "to_dos.txt") -> None:
    """Writes the to-dos to a file.

    Args:
        to_dos_local (List[str]): _description_
        filename (str, optional): _description_. Defaults to "to_dos.txt".
    """
    script_dir = os.path.dirname(__file__)
    to_dos_file = os.path.join(script_dir, filename)

    with open(to_dos_file, "w") as file:
        for item in to_dos_local:
            file.write(item + "\n")

user_prompt: str
user_prompt = "Type add, show, edit, complete or exit: "
to_dos: List[str]
to_dos = get_todos()

user_action: str

while True:
    user_action = input(user_prompt).strip().lower()
    
    if user_action.startswith("add") or user_action.startswith("new") or user_action.startswith("more"):
        user_todo = user_action[4:]
        if not user_todo:
            user_todo = input("Enter a to-do: ")
        to_dos.append(user_todo)
        write_todos(to_dos)
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
                if not user_action[5:]:   
                    to_edit: int = int(input("Enter the number of the to-do you want to edit: "))             
                else:
                    to_edit: int = int(user_action[5:])
                if to_edit > len(to_dos):
                    print("You are out of range.")
                else:
                    new_todo = input("Enter a new to-do: ")
                    to_dos[to_edit - 1] = new_todo
                    write_todos(to_dos)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
    elif user_action.startswith("complete") or user_action.startswith("done") or user_action.startswith("finish")  or user_action.startswith("remove"):
            if not to_dos:
                print("You have no to-dos.") 
            else:               
                try:
                    if not user_action[9:]:
                        to_complete: int = int(input("Enter the number of the to-do you want to complete: "))
                    else:
                        to_complete: int = int(user_action[9:])
                    index: int = to_complete - 1
                    removed_task: str = to_dos[index] 
                    to_dos.pop(index)
                    write_todos(to_dos)
                    message: str = "You have no to-dos." if not to_dos else f"{removed_task} has been removed."
                    print(message)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                except IndexError:
                    print("Invalid input. Please enter a number within the range of number ot all items.")
                    continue
    elif user_action.startswith("exit") or user_action.startswith("quit") or user_action.startswith("stop") or user_action.startswith("end"):
        write_todos(to_dos)
        break
    else:
        print("Invalid input")
    

print(f"You entered: {to_dos}")