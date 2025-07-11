def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Divide by zero error!"

def main():
    while True:
        print("\n---- Calculator ----")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '5':
            print("Exiting calculator.")
            break

        try:
            num1 =

