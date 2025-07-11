def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

num = int(input("Enter number: "))
if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
hbbj
