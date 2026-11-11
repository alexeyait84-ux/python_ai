number = int(input("Введите неотрицательное целое число: "))
j = 0
for i in range(number, 0, -1):
    if i > 2:
        j = j + 1
        print(i)
print("Count: ", j)