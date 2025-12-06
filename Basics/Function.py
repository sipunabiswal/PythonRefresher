print("Hello Welcome to python functions.")#Print is a inbuilt function in python

#Custom Function
def my_function():
    print("This is my first function")

my_function()  # Calling the function 


def greet_user(username):
    print(f"Hello, {username}!")

greet_user("Alice")  # Calling the function with an argument


def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # Calling the function and storing the return value
print(f"The sum is: {result}")


#function example with scope 
def outer_function():
    outer_var = "I am outside!"

    def inner_function():
        inner_var = "I am inside!"
        print(inner_var)  # Accessing inner variable
        print(outer_var)  # Accessing outer variable

    inner_function()
    # print(inner_var)  # This would raise an error because inner_var is not accessible here

outer_function()


def person_info(fname,lname,age):
    person={
        "first_name":fname,
        "last_name":lname,
        "age":age
    }
    return person

person1=person_info("John","Doe",28)
print(person1)