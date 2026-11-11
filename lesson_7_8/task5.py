def greeting(name):
    print("Hello, " + name + "!")

# Variant 1
greeting(input("What is your name? "))
# Если не нужно использовать имя пользователя далее, то
# Variant 2
name = input("What is your name? ")
greeting(name)

