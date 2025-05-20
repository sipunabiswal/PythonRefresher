print("Welcome to the tipp calculator!")
print("This program will help you split the bill between friends.")

total_bill = float(input("Please enter the total bill amount:"))
number_of_people = int(input("Please enter the number of people to split the bill:"))
tip_percentage = float(input("Please enter the tip percentage you would like to give:")) / 100
tip_amount = total_bill * tip_percentage
total_amount = total_bill + tip_amount
amount_per_person = total_amount / number_of_people
print(f"The total bill amount is: {total_bill:.2f}")
print(f"The tip amount is: {tip_amount:.2f}")
print(f"The total amount to be paid individual  is: {amount_per_person:.2f}")