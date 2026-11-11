# import greetings
# Подключаем наш файл greetings.py как модуль.
message = greetings.greet("Анна")
# Вызываем функцию и сохраняем возвращенную строку.
print(message)
# # Выводим полученное приветствие.

# Импортируем функцию по имени

from greetings import greet
# Делаем имя greet доступным в main.py.
message = greet("Иван")
# Вызываем импортированную функцию напрямую.
print(message)
# Выводим возвращенную строку.