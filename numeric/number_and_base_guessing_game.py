import random


def guessing_base():
    answer = random.randint(0, 100)
    base = random.choice(
        [2, 8, 10, 16]
    )  # random base between 2 and 16 (binary, octal, decimal, hexadecimal)
    print(
        f"I'm thinking of a number between 0 and 100. Can you guess what it is in base {base}?"
    )

    while True:
        user_guess = input("Guess the number between 0 and 100: ")
        if user_guess.isdigit():
            user_guess = int(user_guess, base)
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


if __name__ == "__main__":
    guessing_base()
