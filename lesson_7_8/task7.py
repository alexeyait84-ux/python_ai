def input_name():
    name = input("What is your name? ")
    return name

def input_age():
    age = int(input("What is your age? "))
    return age

def user_check(name, age   ):
    if age >= 18:
        print("Hello, " + name + "!")
    else:
        print("You are young!")

print("--------")

user_name = input_name()
user_age = input_age()
user_check(user_name, user_age)
# user_check(input_name(), input_age())