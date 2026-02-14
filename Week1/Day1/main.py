import json
import os

TASK_FILE = "tasks.json"

if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Function to add a task
def add_task(title):
    task = {"title": title, "status": "pending"}
    tasks.append(task)
    save_tasks()
    print(f"Task '{title}' added successfully!")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks()
        print(f"Task '{removed['title']}' deleted successfully!")
    else:
        print("Invalid task number!")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["status"] = "done"
        save_tasks()
        print(f"Task '{tasks[index]['title']}' marked as done!")
    else:
        print("Invalid task number!")

def show_tasks():
    if not tasks:
        print("No tasks available!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✅" if task["status"] == "done" else "❌"
        print(f"{i+1}. {task['title']} - {status}")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Done")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                add_task(title)
            else:
                print("Task title cannot be empty!")
        elif choice == "2":
            show_tasks()
            if tasks:
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    delete_task(index)
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == "3":
            show_tasks()
            if tasks:
                try:
                    index = int(input("Enter task number to mark done: ")) - 1
                    mark_done(index)
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
