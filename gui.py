from modules import functions
import FreeSimpleGUI as sg

add_label = sg.Text("Type in a to-do")
add_input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Completed")

window = sg.Window('My To-Do App', 
                   layout=[[add_label], 
                           [add_input_box, add_button], 
                           [list_box,edit_button, complete_button]], 
                   font=('Helvetica', 16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            to_dos = functions.get_todos()
            user_todo = values['todo']
            to_dos.append(user_todo)
            functions.write_todos(to_dos)
            window['todos'].update(values=to_dos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            to_dos = functions.get_todos()
            index = to_dos.index(todo_to_edit)
            to_dos[index] = new_todo
            functions.write_todos(to_dos)
            window['todos'].update(values=to_dos)
        case sg.WIN_CLOSED:
            break

window.close()
