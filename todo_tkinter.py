import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove a task
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to mark a task as done
def mark_done():
    try:
        selected_task = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task)
        if not task.startswith("✔ "):  
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, f"✔ {task}")
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# Create main window
root = tk.Tk()
root.title("Netflix-Style To-Do List")
root.geometry("500x600")
root.configure(bg="#141414")  # Netflix Dark Background

# Task Entry Field
task_entry = tk.Entry(root, font=("Arial", 14), width=40, fg="white", bg="#222222", insertbackground="white")
task_entry.pack(pady=15)

# Custom Button Styling (Netflix Red Buttons)
def create_button(text, command):
    return tk.Button(root, text=text, command=command,
                     font=("Arial", 12, "bold"), fg="white", bg="#E50914",
                     activebackground="#ff2e2e", activeforeground="white",
                     relief="flat", bd=0, padx=10, pady=5, width=20)

# Buttons
add_button = create_button("➕ Add Task", add_task)
add_button.pack(pady=5)

remove_button = create_button("❌ Remove Task", remove_task)
remove_button.pack(pady=5)

done_button = create_button("✔ Mark as Done", mark_done)
done_button.pack(pady=5)

# Listbox for tasks
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=12, font=("Arial", 14),
                          bg="#222222", fg="white", bd=0, highlightthickness=0)
task_listbox.pack(pady=10)

# Scrollbar for Listbox
scrollbar = tk.Scrollbar(root, orient="vertical", command=task_listbox.yview)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Load tasks on startup
load_tasks()

# Run the GUI
root.mainloop()
