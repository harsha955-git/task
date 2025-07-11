def is_palindrome(s):
    return s == s[::-1]

text = input("Enter text: ").lower().replace(" ", "")
if is_palindrome(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

