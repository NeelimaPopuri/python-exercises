import random
num_ran = random.randint(1, 100)
while True:
    try:
        guess = int(input("guess a random number between 1 to 100:"))
        if guess > num_ran:
            print("Too High")
        elif guess < num_ran:
            print("Too Low")
        else:
            print("Congrations! You guessed the number")
            break
    except ValueError:
        print("enter a valid Number")
