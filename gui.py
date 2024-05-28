from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkAmber')

clock = sg.Text('',key="clock")

add_label = sg.Text("Type in a to-do")
add_input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add to-do", key="Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

complete_button = sg.Button(size=40, image_source="complete.png", mouseover_colors="LightBlue2", tooltip="Select to-do to complete", key="Completed")
exit_button = sg.Button("Exit")

layout = [[clock], [add_label], 
            [add_input_box, add_button], 
            [list_box, edit_button, complete_button],
            [exit_button]]

window = sg.Window('My To-Do App', 
                   layout=layout, 
                   font=('Helvetica', 16))
while True:
    event, values = window.read(timeout=100)
    if event in (sg.WINDOW_CLOSED, None):
        break  # exit loop
    else:
        window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                to_dos = functions.get_todos()
                if not values['todo']:
                    raise IndexError
                user_todo = values['todo']
                to_dos.append(user_todo)
                functions.write_todos(to_dos)
                window['todos'].update(values=to_dos)
            except IndexError:
                sg.popup("Please enter a to-do.", font=('Helvetica', 16))
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                to_dos = functions.get_todos()
                index = to_dos.index(todo_to_edit)
                to_dos[index] = new_todo
                functions.write_todos(to_dos)
                window['todos'].update(values=to_dos)
            except IndexError:
                sg.popup("Please select a to-do to edit.", font=('Helvetica', 16))        
        case "Completed":
            try:
                todo_to_complete = values['todos'][0]
                to_dos = functions.get_todos()
                to_dos.remove(todo_to_complete)
                functions.write_todos(to_dos)
                window['todos'].update(values=to_dos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a to-do to complete.", font=('Helvetica', 16))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
