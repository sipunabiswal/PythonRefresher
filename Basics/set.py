my_set = {1, 2, 3, 4, 5,1,1,2,3,4}
print("Original set:", my_set)

for item in my_set:
    print(item)


my_set.add(6)
print("Set after adding an element:", my_set)

my_set.discard(3)
print("Set after discarding an element:", my_set)   