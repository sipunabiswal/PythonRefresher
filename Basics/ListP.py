#list of 5 animall called zoo
zoo=["lion","tiger","elephant","giraffe","zebra"]
print("Original zoo list:", zoo)
zoo.remove(zoo[3])  # Remove the animal "giraffe"
print("Zoo list after removing giraffe:", zoo)
zoo.append("monkey")  # Add a new animal to the end of the list
print("Zoo list after adding monkey:", zoo)

zoo.remove(zoo[0])  # Remove the animal at index 0 (lion)
print("Zoo list after removing index 0:", zoo)

#slice
print("Sliced zoo list (index 0 to 3):", zoo[0:3])