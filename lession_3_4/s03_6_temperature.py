temperature = int(input("Введите температуру в виде целого числа: "))
if temperature <= 0:
    print("Cold")
elif temperature <= 25:
    print("Normal")
else:
    print("Hot")