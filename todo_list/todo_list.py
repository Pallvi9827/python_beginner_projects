tasks = []

while True:
    print("\n ---- SIMPLE TODO LIST ----")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

    choice= input("Enter your choice (1-4):")

    if choice == '1':
        if not tasks:
            print("No tasks yet.")

        else:
            for i,task in enumerate(tasks, start=1):
                print(f"{i} , {task}")

    elif choice == '2':
        task= input("Enter task name:")
        tasks.append(task)
        print(f"Task '{task}' added.")

    elif choice == '3':
        if not tasks:
            print("NO tasks to mark as done.")

        else:
            for i, task in enumerate(tasks, star3t=1):
                print(f"{i},{task}")

            try:
                task_no = int(input("Enter task number to mark as done:"))
                removes= tasks.pop(task_no-1)
                print(f"task '{removes}' marked as done and removed.")
            except(ValueError, IndexError):
                print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.please enter a number between 1-4.")
        



