terms = int(input("How many Fibonacci terms? "))
a, b = 0, 1
count = 0
print("Fibonacci sequence:")
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

