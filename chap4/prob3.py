import random
num = random.randrange(1,100)
counter = 0
answer = 0
print("           Welcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as poosible.\n")
while answer != num :
 answer = int(input("Take a guess: "))
 if answer > num :
    print("Lower...")
 elif answer < num :
    print("Higher!")
 counter += 1
print("You guessed it! The number was ", num)
print("And it only took you ", counter, " tries!")
print("\n\nPress the enter key to quit.")

