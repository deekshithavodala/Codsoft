import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        pass

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create and configure the listbox to display tasks
task_listbox = tk.Listbox(app)
task_listbox.pack(pady=50)

# Create an entry widget to input new tasks
task_entry = tk.Entry(app)
task_entry.pack(pady=50)

# Create buttons to add and delete tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)

# Add the buttons to the GUI
add_button.pack(pady=20)
delete_button.pack(pady=20)

# Increase the size of the to-do list window
app.geometry("500x300")

# Start the tkinter main loop
app.mainloop()