my_list =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# while my_list:
#     day = my_list.pop(0)
#     print("Today is:", day)

#Create a while loop that prints all elements of the my_list variable 3 times

# while my_list:
#     day = my_list.pop(0)
#     for _ in range(3):
#         print("Today is:", day)
x=0 
while x < 3:
    for day in my_list:
        print("Today is:", day)
    x += 1

# for day in my_list:
#     if day != "Monday":
#         print("Today is:", day)