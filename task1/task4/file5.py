import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    try:
        t = int(input("Enter countdown time in seconds: "))
        countdown(t)
    except ValueError:
        print("Please enter a valid number.")

main()

