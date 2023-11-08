print("Input your string...")

def Open(file):
    print("\n\n\nYour inputs are below..")
    text_file = open(file,"r")
    whole_thing = text_file.read()
    print(whole_thing)

def write(file, string):
    text_file = open(file, "a")
    text_file.write(string + "\n")
    text_file.close()

file = "text.txt"
open(file, "w").close()

while True:
    string = input(">> ")
    if string.upper() == 'Q':
        print("Write process has been finished")
        break
    else:
        write(file, string)

Open(file)
