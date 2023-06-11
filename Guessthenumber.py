import random

def play_game(level):
    if level == "easy":
        max_range = 50
        max_attempts = 8
    elif level == "hard":
        max_range = 100
        max_attempts = 5
    else:
        print("Invalid level. Please choose 'easy' or 'hard'.")
        return

    random_number = random.randint(1, max_range)

    print("Welcome to the {level} level!")
    print("Number between 1 and {max_range}.")
    print("You have {max_attempts} attempts to guess the number.")

    for attempt in range(max_attempts, 0, -1):
        number = int(input("Enter a number: "))

        if number == random_number:
            print("Congratulations! You guessed the right number!")
            return
        elif number < random_number:
            print("Guess higher.")
        elif number > random_number:
            print("Guess lower.")

        if attempt > 1:
            print(f"You have {attempt - 1} attempts left.")
        else:
            print("Out of attempts. You lost. Try again!")

level_choice = input("Choose a level (easy/hard): ")
play_game(level_choice)
