# text = "Hello"
# digits = "123"
# number = 123
# print(text)
# print(digits + "1")
# print(number + 1)
# print(len(digits))
# print(digits + 1)
# print(int(digits))
#
# Положительные и отрицательные индексы
# text = "Python"
# print(text[0])
# print(text[3])
# print(text[-1])
# print(text[-2])
#
# Длина и безопасное чтение пустой строки
# text = "Python"
# print("Length:", len(text))
# if len(text) > 0:
#     print("First:", text[0])
#     print("Last:", text[-1])
# else:
#     print("Empty text")
#
# Срез выбирает часть строки
# text = "Hello"
# print(text[1:4])
# print(text[:3])
# print(text[3:])
# print(text[:])
# print("Empty: [" + text[2:2] + "]")

# text[start:stop]
# Шаг среза и движение назад
text = "Hello World!"
print(text[2])
print(text[-2])
print(text[1:4])
print(text[7:3:-1])
print(text[::2])
print(text[::-1])
# У среза есть третий параметр: [start:stop:step]
# У среза есть третий параметр: [start:stop:step].
# Шаг 2 пропускает каждый второй символ, шаг -1 движется назад.
# Граница stop остается исключенной. Для разворота всей строки подходит [::-1].

# Объединение и повторение текста
# first_name = "Ivan"
# last_name = "Petrov"
# full_name = first_name + " " + last_name
# print(full_name)
# print("Hello, " + full_name)
# print("!" * 3)
# print("[" + "Hi " * 3 + "]")
#
# Списки
# name1 = "Anna"
# name2 = "Ivan"
# name3 = "Oleg"
# names = ["Anna", "Ivan", "Oleg"]
# print(names)
#
# Создание списка и количество элементов
cities = ["Berlin", "Paris", "London"]
numbers = [10, 20, 30]
empty = []
print(cities)
print(len(cities))
print(numbers)
print(len(empty))
print(list("abc"))
print(list[str]("Berlin, Paris, London"))
print(list("Berlin, Paris, London"))

