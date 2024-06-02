import streamlit as st
from modules import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_todos(todos)



st.title("My To-do App")

st.subheader("Developed by M. Galchenkova")

st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a new to-do", placeholder="Add a new to-do", label_visibility="hidden", on_change=add_todo, key="new_todo")

