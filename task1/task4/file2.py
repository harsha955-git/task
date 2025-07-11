def add_student(data):
    name = input("Enter student name: ")
    grades = input("Enter grades separated by space: ").split()
    grades = list(map(float, grades))
    data[name] = grades

def display_students(data):
    for name, grades in data.items():
        avg = sum(grades)/len(grades)
        print(f"{name}: Grades: {grades}, Average: {avg:.2f}")

def main():
    students = {}
    while True:
        print("\n1. Add Student\n2. Display All\n3. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

main()

