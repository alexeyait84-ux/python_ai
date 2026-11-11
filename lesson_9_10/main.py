# Путь и создание пустого файла
# from pathlib import Path
#
# BASE = Path(__file__).resolve().parent
# path = BASE / "e01_marker.txt"
# print("Name:", path.name)
# print("Suffix:", path.suffix)
# print("Stem:", path.stem)
# print("Before:", path.exists())
# path.touch()
# print("After:", path.exists())

# from pathlib import Path
#
# BASE = Path(__file__).resolve().parent
# folder = BASE / "e02_data" / "first" / "second"
# folder.mkdir(parents=True, exist_ok=True)
# # Для записи во вложенную папку сначала создаем ее через mkdir()
# # parent=True создает недостающие родительские папки
# # exist_ok=True допускает уже существующую папку
# path = folder / "note.txt"
# path.touch()
# print("Folder:", folder.is_dir())
# print("File:", path.is_file())
#
# Запись русского текста и блок with

# from pathlib import Path
#
# BASE = Path(__file__).resolve().parent
# path = BASE / "e03_note.txt"
#
# # Открываем файл для записи.
# with open(path, "w", encoding="utf-8") as file:
#     written = file.write("Привет, файл!")
#
# # Запись завершена, файл закрыт.
# print("Written:", written)
# print("После записи закрыт:", file.closed)
#
# # Снова открываем тот же файл, теперь для чтения.
# with open(path, "r", encoding="utf-8") as file:
#     content = file.read()
#
# # Чтение завершено, файл снова закрыт.
# print("После чтения закрыт:", file.closed)
# print(content)

# from pathlib import Path
#
# BASE = Path(__file__).resolve().parent
# folder = BASE / "e02_data" / "first"
#
# max_size = -1
# file_name = None
# for file in folder.glob("*"):
#     if file.is_file():
#         if file.stat().st_size > max_size:
#             max_size = file.stat().st_size
#             file_name = file.name
#
# if file_name is None:
#     print("У нас нет файлов в папке")
# else:
   #  print(f"{file_name}: {max_size}")
#         print(file.name)
# folder = BASE / "e02_data" / "first" / "second"
# folder.mkdir(parents=True, exist_ok=True)
# # Для записи во вложенную папку сначала создаем ее через mkdir()
# # parent=True создает недостающие родительские папки
# # exist_ok=True допускает уже существующую папку
# path = folder / "note.txt"
# path.touch()
# print("Folder:", folder.is_dir())
# print("File:", path.is_file())

from pathlib import Path
# #
# BASE = Path(__file__).resolve().parent
#
# for file in BASE.glob("*"):
#     if file.is_file():
#         print(file.name)

from pathlib import Path

# Создадим файл в заданной папке и напишем в него
# числа от 1 до 10, что каждое число находится в своей строчке
def create_simple_counter_file(folder):
    filename = folder / "1bis10.txt"
    filename.touch(exist_ok=True)
    with open(filename, "w") as f:
        for i in range(10):
            f.write(str(i + 1))
            f.write("\n")

"""# Читает файл и выдает самое большое число в файле
# Каждое число находится в отдельной строке
def print_biggest_number(filename):
    max_num = 0
    with open(filename, "r") as f:
        print(f.readlines())"""

if __name__ == "__main__":
    BASE = Path(__file__).resolve().parent
    folder = BASE / "e02_data"

    create_simple_counter_file(folder) # вызов функци

