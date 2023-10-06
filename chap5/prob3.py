import random
print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.")
words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
word = random.choice(words)
length = len(word)
print("\n\nLength of the selected word:", +length)
ra = int(6)
answer = ''
while 0 < ra :
    fail = 0
    print("Current guessed word:", end='')
    for char in word :
        if char in answer :
            print(char,"", end='')
        else :
            print("_ ", end='')
            fail += 1
    
    if fail == 0 :
        print("\nCongratulations! You guessed the word:", word)
        break
    guess = input("\nGuess a letter: ")
    answer += guess
    if guess not in word :
        ra -= 1
        print("Incorrect guess.")
        print("Remaining attempts:",+ra)
