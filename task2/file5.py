text = input("Enter text: ").lower()
vowels = "aeiou"
v, c = 0, 0
for char in text:
    if char.isalpha():
        if char in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v)
print("Consonants:", c)

