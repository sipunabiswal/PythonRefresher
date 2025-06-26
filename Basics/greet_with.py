def greet_with(name,location):
    print(f"Hello {name} from {location}!")
    
greet_with("Alice", "Wonderland")



#named parameter
def greet_with_named(name : str, location: str) :
    print(f"Hello {name} from {location}!")

greet_with_named(name="Bob", location="Builderland")
greet_with_named(location="Builderland", name="Bob")  # Order doesn't matter with named parameters