score = int(input("Введите оценку от 0 до 100: "))
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")