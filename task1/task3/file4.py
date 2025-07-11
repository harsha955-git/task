def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View\n2. Add\n3. Remove\n4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '2':
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    save_tasks(tasks)
                else:
                    print("Invalid number.")
            except:
                print("Invalid input.")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

main()

