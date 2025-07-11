def count_words(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
        words = text.split()
        print(f"Total words: {len(words)}")
    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        file = input("Enter filename (or 'exit'): ")
        if file == 'exit':
            break
        count_words(file)

main()

