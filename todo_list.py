def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        try:
            index = int(input("Enter task number to remove: "))
            removed = tasks.pop(index - 1)
            print(f"{removed} removed successfully.")
        except:
            print("Invalid task number.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
