import operator

c = ''
geek = {"404" : "clueless.",
        "Uninstalled" : "being fired.    Especially popular during the dot-bomb era."}

while c != 0 :
    i = int(0)

    print("     \nGeek Translator\n")
    print("     1 - Look Up a Geek Term")
    print("     2 - Add a Geek Term")
    print("     3 - Redefine a Geek Term")
    print("     4 - Delete a Geek Term")
    c = int(input("\nChoice: "))
    if c == 1 :
        term = input("\nWhat term do you want me to translate?: ")
        if term in geek:
            mean = geek[term]
            print("\n", term, "means", mean)
        else :
            print("\nI have no idea what", term, "is")
    elif c == 2 :
        term = input("What term do you want me to add?: ")
        if term not in geek:
            mean = input("\nwhat does it mean?: ")
            geek[term] = mean
        else:
            print("\nIt has already been added.")
    elif c == 3 :
        term = input("\nWhat term do you want me to redefine?: ")
        if term in geek:
            mean = input("What's the new definition?: ")
            geek[term] = definition
        else:
            print("\nIt doesn't exist.")
    elif c == 4 :
        term=input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print("\n", term, "is deleted")
        else:
            print("\nIt doesn't exist.")
    else:
        print("Please enter the number from the list.")
    
