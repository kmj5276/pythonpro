import random
mood = random.randrange(3)
print("I sense your energy. Your true emotions are coming across my screen.")
print("You are...")
if mood == 0 :
 # happy
 print("          ------------")
 print("          |          |")
 print("          | O      O |")
 print("          |   <      |")
 print("          | .      . |")
 print("          |  *....*  |")
 print("          ------------")
elif mood == 1 :
 # neutral
 print("           ------------")
 print("           |          |")
 print("           | --    -- |")
 print("           |   <      |")
 print("           |          |")
 print("           |   ----   |")
 print("           ------------")
elif mood == 2 :
 # sad
 print("           ------------")
 print("           |          |")
 print("           | __    __ |")
 print("           | : <    : |")
 print("           | '      ' |")
 print("           | .''''''. |")
 print("           ------------")
else :
 # not draw
 print("Illegal mood value!")
print("...today.")
print("\nPress the enter key to quit.")
