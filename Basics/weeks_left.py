def life_in_weeks(curr_age):
    years_left= 90-curr_age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")
    
curr_age = int(input("Enter your current age : "))
life_in_weeks(curr_age)