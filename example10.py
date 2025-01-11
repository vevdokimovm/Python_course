def greet_name(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name")
        
print(greet_name("Anton"))
print(greet_name("anton"))