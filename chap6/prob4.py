HANGMAN = [
    """
    ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------""",
    """
    ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------""",
    """
    ------
     |    |
     |    O
     |    |
     |
     |
     |
     |
     |
    ----------""",
    """
    ------
     |    |
     |    O
     |   -|-
     |
     |
     |
     |
     |
    ----------""",
    """
    ------
     |    |
     |    O
     |   -|-
     |   /
     |
     |
     |
     |
    ----------""",
    """
    ------
     |    |
     |    O
     |   -|-
     |   / \\
     |
     |
     |
     |
    ----------""",
]

MAX_WRONG = len(HANGMAN) - 1

word = "PYTHON"

so_far = "-" * len(word)
wrong = 0
used = []

def display_hangman(wrong):
    print(HANGMAN[wrong])

print("Welcome to Hangman.")

while wrong < MAX_WRONG and so_far != word:
    display_hangman(wrong)
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)
    guess = input("\n\nEnter your guess: ").upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ").upper()

    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    display_hangman(wrong)
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit.")
