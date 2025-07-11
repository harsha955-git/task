import string

def check_strength(password):
    length = len(password) >= 8
    lower = any(c in string.ascii_lowercase for c in password)
    upper = any(c in string.ascii_uppercase for c in password)
    digit = any(c in string.digits for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, lower, upper, digit, special])
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    while True:
        pwd = input("Enter password (or 'exit'): ")
        if pwd.lower() == 'exit':
            break
        print("Strength:", check_strength(pwd))

main()

