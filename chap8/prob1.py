print("Opening and closing the file.\n")
print("Reading characters from the file.")
text_file = open("read.txt","r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading the entire file at once.")
text_file = open("read.txt","r")
whole_thing = text_file.read()
print(whole_thing)

print("\nReading characters from a line.")
text_file = open("read.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time.")
text_file = open("read.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nReading the entire file into a list.")
text_file = open("read.txt", "r")
lines = text_file.readlines()
print(lines)
text_file = open("read.txt","r")
print(3)
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nLooping through the file, line by line.")
text_file = open("read.txt", "r")
for line in text_file:
    print(line)
print("\nPress the enter key to exit.")
