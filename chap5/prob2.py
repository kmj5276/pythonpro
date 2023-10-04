import random
print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
word = random.choice(words)
answer = word
word =list(word)
random.shuffle(word)
print("Jumbled word: ", end='')
for i in word:
    print(i, end='')
guess = input("\nYour guess: ")
if answer == guess :
    print("Congratulations! that's correct. The word was: ", answer)
else :
    print("Sorry, that's not correct. The word was: ", answer)

