import operator

c = ''
ns = {
    "Moe": 1000,
    "Larry": 1500,
    "Curly": 3000
}

while c != 0:
    print("     \nHigh Scores Keeper\n")
    print("     0 - Quit")
    print("     1 - List Scores")
    print("     2 - Add a Score")
    c = int(input("\nChoice: "))

    if c == 2:
        name = input("\nWhat is the player's name?: ")
        score = int(input("What score did the player get?: "))
        ns[name] = score
    elif c == 1:
        print("\nHigh Scores")
        print("NAME\tSCORE")
        sorted_ns = sorted(ns.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_ns:
            print(name, "\t", score)
        print("\n")
    else :
        print("Please enter the number from the list.")
