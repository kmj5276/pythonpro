try:
     num = float(input("Enter a number: "))
except:
    print ("Something went wrong!\n")

try:
    num = float(input("Enter a number: "))
except(ValueError):
    print ("That was not a number!\n")

for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "-->", end ='')
        print (float(value))
    except(TypeError, ValueError):
        print ("Something went wrong!")
print("")

for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "-->", end ='')
        print (float(value))
    except(TypeError):
        print ("I can only convert a string or a number!")
    except(ValueError):
        print ("I can only convert a string of digits!")


try:
    num = float(input("\nEnter a number: "))
    e = float(num) 
except ValueError as e:
    print ("That was not a number!  Or as Python would say:\n", e)

while True:
    try:
        num = float(input("\nEnter a number: "))
    except(ValueError):
        print ("That was not a number!")
    else:
        print ("You entered the number", num)
        break


print("\n\nPress the enter key to exit.")
