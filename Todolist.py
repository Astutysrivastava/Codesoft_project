import tkinter as tk
from tkinter import messagebox
import json

# File to save tasks
TASK_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(task_list):
    with open(TASK_FILE, "w") as file:
        json.dump(task_list, file, indent=4)

# Add task
def add_task():
    description = task_entry.get().strip()
    priority = priority_var.get()
    deadline = deadline_entry.get().strip()

    if not description:
        messagebox.showwarning("Input Error", "Task description cannot be empty!")
        return

    task = {
        "description": description,
        "priority": priority,
        "deadline": deadline,
        "status": "Pending"
    }
    task_list.append(task)
    save_tasks(task_list)
    refresh_task_list()
    task_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Task added successfully!")

# Refresh task list
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(task_list, 1):
        status = f"{task['description']} - {task['priority']} - {task['status']}"
        if task["deadline"]:
            status += f" - {task['deadline']}"
        task_listbox.insert(tk.END, f"{i}. {status}")

# Mark task as completed
def mark_as_completed():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No task selected!")
        return
    index = selected[0]
    task_list[index]["status"] = "Completed"
    save_tasks(task_list)
    refresh_task_list()
    messagebox.showinfo("Success", "Task marked as completed!")

# Delete task
def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No task selected!")
        return
    index = selected[0]
    task_list.pop(index)
    save_tasks(task_list)
    refresh_task_list()
    messagebox.showinfo("Success", "Task deleted successfully!")

# Main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")

# Load tasks
task_list = load_tasks()

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_label = tk.Label(input_frame, text="Task Description:")
task_label.grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(input_frame, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5)

priority_label = tk.Label(input_frame, text="Priority:")
priority_label.grid(row=1, column=0, padx=5, pady=5)
priority_var = tk.StringVar(value="Low")
priority_menu = tk.OptionMenu(input_frame, priority_var, "High", "Medium", "Low")
priority_menu.grid(row=1, column=1, padx=5, pady=5)

deadline_label = tk.Label(input_frame, text="Deadline (YYYY-MM-DD):")
deadline_label.grid(row=2, column=0, padx=5, pady=5)
deadline_entry = tk.Entry(input_frame, width=20)
deadline_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Task list frame
task_list_frame = tk.Frame(root)
task_list_frame.pack(pady=10)

task_listbox = tk.Listbox(task_list_frame, width=70, height=15)
task_listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(task_list_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

# Action buttons
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

complete_button = tk.Button(action_frame, text="Mark as Completed", command=mark_as_completed)
complete_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(action_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=10)

# Load and display tasks
refresh_task_list()

# Run the application
root.mainloop()
