"""
Dictionary example demonstrating basic operations
"""

# Creating a dictionary
user_dict={
    "name": "Alice",
    "age": 30,
    "username": "alice123"
}

user_dict["email"] = "alice@example.com"
print("User Dictionary:", user_dict)

# Accessing values
print("Name:", user_dict["name"])
print("Age:", user_dict.get("age"))

# Updating values
user_dict["age"] = 31
print("Updated Age:", user_dict["age"])

# Deleting a key-value pair
del user_dict["username"]

print("Dictionary after deletion:", user_dict)

# Iterating through the dictionary
for key, value in user_dict.items():
    print(f"Iterating {key}: {value}")


# Checking if a key exists
if "email" in user_dict:
    print("Email exists in the dictionary.")


#pop method
removed_email = user_dict.pop("email", "No email found")
print("Removed Email:", removed_email)
print("User Dictionary:", user_dict)


#dict copy method
user_dict_copy = user_dict.copy()
user_dict_copy["name"] = "Bob"
print("Copied Dictionary:", user_dict_copy)

user_dict["address"] = "123 Main St"
print("User Dictionary:", user_dict)