
todo_List = []


def add_task():
    task = input("Enter a task: ")

    todo_List.append({
        "Task": task,
        "status": "pending"
    })

    print("New task added successfully!\n")


def view_task():
    print("\nView Todo List")

    if len(todo_List) == 0:
        print("No tasks found!")
    else:
        for index, task in enumerate(todo_List, 1):
            print(f"{index}: {task['Task']} - {task['status']}")

    print()


def remove_task():
    if len(todo_List) == 0:
        print("List is empty...")
        return

    try:
        task_number = int(input("Enter the task number that you want to remove: "))

        if 1 <= task_number <= len(todo_List):
            removed_task = todo_List.pop(task_number - 1)
            print(f"Task removed: {removed_task['Task']}\n")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid task number!")


def mark_done():
    if len(todo_List) == 0:
        print("List is empty...")
        return

    try:
        task_number = int(input("Enter the task number to mark as completed: "))

        if 1 <= task_number <= len(todo_List):
            todo_List[task_number - 1]["status"] = "completed"
            print("Task marked as completed![✓]\n")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid task number!")


def menu():
    while True:
        print("** Main Menu **")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_task()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            mark_done()

        elif choice == "5":
            print("Exiting the application...")
            break

        else:
            print("Invalid choice! Try again.\n")

menu()
