import random

WORDS = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tomato", "ugli", "violet", "watermelon", "xigua", "yellow", "zucchini"]

def is_digit_input(text):
    while True:
        s = input(text)
        if s.isdigit():
            return int(s)
        else:
            print("Please enter a number!")
            continue

def guessing_word():
    print(f"I'm thinking of a word. Can you guess what it is?")
    print(f"Let's define how many letters it will have.")
    min_length = is_digit_input("Minimum length: ")
    while True:
        max_length = is_digit_input("Maximum length: ")
        if min_length > max_length:
            print("Minimum length must be less than or equal to maximum length!")
            continue
        else:
            break
    defined_words = []
    for word in WORDS:
        if min_length <= len(word) <= max_length:
            defined_words.append(word)
    answer = random.choice(defined_words)
    print(f"The word is {len(answer)} letters long.")

    while True:
        user_guess = input("What is your guess?: ")
        if user_guess == answer:
            print(f"Right! You guessed it! The word was {user_guess}")
            break

        elif user_guess < answer:
            print(f"Your guess of {user_guess} is earlier in the dictionary!")
        else:
            print(f"Your guess of {user_guess} is later in the dictionary!")


if __name__ == "__main__":
    guessing_word()
