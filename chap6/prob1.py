inventory = ["sword", "armor", "shield", "healing potion"]
print("Your items:")
i = 0
while i < 4 :
    print(inventory[i])
    i += 1
print("\nPress the enter key to continue.")
print("You have", len(inventory), "items in your possession")

print("\nPress the enter key to continue.")
if "healing potion" in inventory :
    print("You will live to fight another day")

a = int(input("\nEnter the index number for an item in inventory: "))
print("At index", a, "is", inventory[a])

bs = int(input("\nEnter the index number to begin a slice: "))
es = int(input("Enter the index number to end the slice: "))
print("inventory[ %s : %s ]               %s"  %(bs, es, inventory[bs:es]))

print("\nPress the enter key to continue.")
chest = ("gold", "gem")
print("You find a chest.  It contains:")
print(chest[:])
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory[:])

print("\nPress the enter key to continue.")
print("You trade your", inventory[0], "for a crossbow")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

print("\nPress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)

print("\nPress the enter key to continue.")
print("In a great battle, your", inventory[2], "is destroyed.")
print("Your inventory is now:")
del inventory[2]
print(inventory)

print("\nPress the enter key to continue.")
print("Your", inventory[0], "and", inventory[1], "are stolen by thieves.")
print("Your inventory is now:")
del inventory[:2]
print(inventory)
print("\n\nPress the enter key to exit")
