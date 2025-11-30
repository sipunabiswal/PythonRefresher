"""
Gradeing system using boolean and operators
"""



grade_input = int(input("Enter your grade percentage: "))


is_A = grade_input >= 90
is_B = 80 <= grade_input < 90   
is_C = 70 <= grade_input < 80
is_D = 60 <= grade_input < 70
is_F = grade_input < 60

if is_A:
    print("You received an A!")
elif is_B:
    print("You received a B!")
elif is_C:
    print("You received a C!")
elif is_D:
    print("You received a D!")
elif is_F:
    print("You received an F!")
else:
    print("Invalid grade input.")