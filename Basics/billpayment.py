import my_module as randompick
import random
friends = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
pick = randompick.pick_randomnumber()
print(f"Randomly selected friend: {friends[pick]}")


print("Random bill Payment: " + random.choice(friends))

