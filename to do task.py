import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for idx, (task_id, task) in enumerate(tasks.items(), start=1):
        print(f"{idx}. {task['name']} - {'Done' if task['completed'] else 'Pending'}")

# Add a new task
def add_task(tasks):
    name = input("Enter task name: ")
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {'name': name, 'completed': False}
    save_tasks(tasks)
    print("Task added.")

# Edit an existing task
def edit_task(tasks):
    display_tasks(tasks)
    task_id = input("Enter the number of the task to edit: ")
    if task_id in tasks:
        new_name = input("Enter new task name: ")
        tasks[task_id]['name'] = new_name
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Task not found.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_id = input("Enter the number of the task to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Task not found.")

# Mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    task_id = input("Enter the number of the task to mark as completed: ")
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Task not found.")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
