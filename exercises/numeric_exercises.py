import random
def guessing_game():
    random_number = random.randint(1, 100)
    guess = None
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    print("Congratulations! You've guessed the number.")

    # Start the game
guessing_game()

def beyond_guessing_game():
    random_number = random.randint(1,30)
    
    counter = 0
    while True:
        guess = int(input("Guess a number between 1 and 30: "))
        base = int(input("Enter the base for your number system (e.g., 2 for binary, 16 for hexadecimal): "))
        
        if counter >= 3:
            print(f"Sorry, you've used all your attempts. The number was {random_number}.")
            break

        if guess == random_number:
            print("Congratulations! You've guessed the number.")
            break
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

        counter += 1
