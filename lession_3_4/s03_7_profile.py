name = input("Введите имя: ")
age = int(input("Введите возраст (неотрицательное целое число): "))
print(name)
if age <= 17:
    print("Child")
elif age <= 65:
    print("Adult")
else:
    print("Senior")
print("Profile complete")