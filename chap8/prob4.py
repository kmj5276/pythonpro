import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"] 
brand = ["Claussen", "Heinz", "Vlassic"] 

pickle_file = open("pickles1.dat", "wb")
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()

print("\nUnpickling lists.")
pickle_file = open("pickles1.dat", "rb")
variety = pickle.load(pickle_file)
print(variety)
shape = pickle.load(pickle_file)
print(shape)
brand = pickle.load(pickle_file) 
print(brand)
pickle_file.close()

print("\nShelving lists.")
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]
pickles.sync()

print("\nRetrieving lists from a shelved file:")
print("brand -", pickles["brand"])
print("shape -", pickles["shape"])
print("variety -", pickles["variety"])
pickles.close()

print("\n\nPress the enter key to exit.")
