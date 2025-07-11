def is_palindrome(sentence):
    clean = ''.join(c.lower() for c in sentence if c.isalnum())
    return clean == clean[::-1]

def main():
    while True:
        text = input("Enter a sentence (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        if is_palindrome(text):
            print("It's a palindrome.")
        else:
            print("Not a palindrome.")

main()

