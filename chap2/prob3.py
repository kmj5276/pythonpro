name = input("Hi. What's your name? ")
old = int(input("And how old are you? "))
weight = int(input("Okay, last question. How many pounds do you weigh? "))
dog = int(old/7)
sec = old*31536000
print("\nDid you know that you're just", dog, "in dog years?")
print("\nBut you're also over", sec, "seconds old.")
print("\nIf a small child were trying to get your attention, your name would become:")
print(name*5)
moon = weight/6
print("\nDid you know that on the moon you would weigh only", moon,"pounds?")
sun = weight*27.1
print("But on the sun, you'd weight", sun, "<but, ah... not for long>.")

