import random

secret = random.randint(1, 20)
attempts = 0
print("Guess the number between 1 and 20.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == secret:
        print(f"Correct! You guessed in {attempts} tries.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

