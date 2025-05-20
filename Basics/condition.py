print("Welcome to the rollercoaser!")
height = int(input("Please enter your height in cm:"))
bill=0
if height>=120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age:"))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
            bill = 12

    want_photo = input("Do you want a photo taken? (Y/N): ").strip().upper()
    if want_photo == "Y":
        bill += 3
   
    print(f"Your total bill is: ${bill}")
    print("Enjoy your ride!")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")
    print("You need to be at least 120 cm tall to ride.")



# The code above is a simple program that checks if a person is tall enough to ride a rollercoaster.
# #Modulo operator
# The modulo operator (%) is used to find the remainder of a division operation.
# For example, 7 % 3 = 1 because when you divide 7 by 3, the remainder is 1.




