#Add 3 motorcycle elements in a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
#print the motorcycles list to console
print(f"\nInitial number of motorcycles list: {motorcycles} \n")

popped_motorcycle = motorcycles.pop()
print(f"After popping the motorcycles, the initial object becomes: {motorcycles}\n")
print(f"Popped motorcycle from initial list: {popped_motorcycle}")

popped_motorcycle2 = motorcycles.pop()
print(f"After popping the motorcycles, the initial object becomes: {motorcycles}\n")
print(f"Popped motorcycle during first occurence: {popped_motorcycle}")
print(f"Popped motorcycle during second occurence: {popped_motorcycle2}")
