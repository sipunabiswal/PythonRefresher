def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = sum(combined_names.count(char) for char in "true")
    love_count = sum(combined_names.count(char) for char in "love")
    score = int(f"{true_count}{love_count}")
    return score

name1 = "Angela Yu"
name2 = "Jack Bauer"

love_score = calculate_love_score(name1, name2)
print(f"Your love score is {love_score}.")