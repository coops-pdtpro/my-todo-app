import os
import streamlit as st
import functions

# Set the desired working directory
os.chdir("C:/Users/coope/PycharmProjects/todo-app/app1/venv")

# Retrieve todos from file
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear input field after adding
    st.experimental_rerun()  # Trigger a rerun to update the UI


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Create a list to track checkboxes state
checkboxes = st.session_state.get("checkboxes", {})

for index, todo in enumerate(todos):
    # Use checkboxes, initialize from session state
    checkbox_state = checkboxes.get(todo.strip(), False)
    checkbox = st.checkbox(todo, value=checkbox_state, key=todo)

    if checkbox and not checkbox_state:
        # Mark todo as complete
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # Remove todo from session state
        checkboxes[todo.strip()] = True  # Mark as completed in session state

# Update session state with current checkboxes state
st.session_state["checkboxes"] = checkboxes

# If the user has clicked the checkbox, rerun to refresh the state
if any(checkboxes.values()):
    st.experimental_rerun()

# Input box to add new todos
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
