import random


def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input("Guess the number between 0 and 100: "))

        if user_guess == answer:
            print(f"Right! You guessed it! The number was {user_guess}")
            break

        elif user_guess < answer:
            print(f"Your guess of {user_guess} is too low!")
        else:
            print(f"Your guess of {user_guess} is too high!")


def modified_guessing_game():
    answer = random.randint(0, 100)
    i = 0
    while i < 3:
        user_guess = input("Guess the number between 0 and 100: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == answer:
                print(f"Right! You guessed it! The number was {user_guess}")
                break

            elif user_guess < answer:
                print(f"Your guess of {user_guess} is too low!")
            else:
                print(f"Your guess of {user_guess} is too high!")
        else:
            print("Please enter a number!")
            continue

        i += 1
    else:
        print("You didn't guess in time, sorry!")


if __name__ == "__main__":
    modified_guessing_game()
