# macOS и Linux
# mkdir Lesson_18
# cd Lesson_18
# python3 -m venv .venv
# .venv/bin/python -m pip install --upgrade pip
# .venv/bin/python -m pip install sentence-transformers numpy scikit-learn
#
# Windows PowerShell
# mkdir Lesson_18
# cd Lesson_18
# py -m venv .venv
# & .\.venv\Scripts\python.exe -m pip install --upgrade pip
# & .\.venv\Scripts\python.exe -m pip install sentence-transformers numpy scikit-learn
#
# Windows CMD
# mkdir Lesson_18
# cd Lesson_18
# py -m venv .venv
# .venv\Scripts\python.exe -m pip install --upgrade pip
# .venv\Scripts\python.exe -m pip install sentence-transformers numpy scikit-learn

# from sentence_transformers import SentenceTransformer
# # Импортируем класс для создания объекта модели.
# model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu", local_files_only=True)
# # Загружаем модель для английских учебных текстов на обычный процессор.
# embedding = model.encode("Hello World!", show_progress_bar=False)
# # Получаем один вектор из одной переданной строки.
# print(embedding.shape)
# # Выводим форму массива одного embedding.
# texts = ["shipping", "delivery", "cat"]
# # Подготавливаем три текста в определенном порядке.
# embeddings = model.encode(texts, show_progress_bar=False)
# # Получаем одну строку координат на каждый текст списка.
# print(embeddings.shape)
# # Проверяем число строк и число координат в каждой строке.
# print(embeddings[0].shape)
# Берем первую строку, то есть вектор текста shipping.

# from sentence_transformers import SentenceTransformer
# # Подключаем загрузку модели embeddings.
# from sklearn.metrics.pairwise import cosine_similarity
# # Подключаем вычисление сходства для строк числовых таблиц.
# model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
# # Создаем одну модель до кодирования всех слов примера.
# texts = ["shipping", "delivery", "banana"]
# # Берем два слова о доставке и одно слово о фрукте.
# vectors = model.encode(texts, show_progress_bar=False)
# # Получаем таблицу из трех векторов в порядке texts.
# near = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
# # Сравниваем shipping с delivery и достаем числовую оценку.
# far = cosine_similarity([vectors[0]], [vectors[2]])[0][0]
# # Сравниваем shipping с banana той же операцией.
# print(f"shipping / delivery: {near:.3f}")
# # Печатаем первую оценку с тремя знаками после точки.
# print(f"shipping / banana: {far:.3f}")
# # Печатаем вторую оценку в том же формате.

from sentence_transformers import SentenceTransformer
# Подключаем класс моделей для получения embeddings.
from sklearn.metrics.pairwise import cosine_similarity
# Подключаем функцию сравнения векторов.
name = "paraphrase-multilingual-MiniLM-L12-v2"
# Выбираем многоязычную модель из русского примера архива.
model = SentenceTransformer(name, device="cpu")
# Загружаем ее один раз перед кодированием трех фраз.
texts = []
# Создаем список фраз в заранее известном порядке.
texts.append("Я попал в ДТП и повредил свой автомобиль")
# Добавляем описание автомобильной аварии.
texts.append("Со мной случилась авария, помял крыло моей машины")
# Добавляем ту же тему, выраженную другими словами.
texts.append("Я отлично прогулялся вчера пешком и отдохнул")
# Добавляем фразу о прогулке для сравнения.
vectors = model.encode(texts, show_progress_bar=False)
# Превращаем все три фразы в строки числовой таблицы.
scores = cosine_similarity([vectors[0]], vectors)[0]
# Сравниваем первую фразу со всеми тремя и берем строку оценок.
for index, score in enumerate(scores):
# Перебираем позицию и оценку каждого сравниваемого текста.
    print(index, f"{score:.3f}")
    # Печатаем индекс фразы и ее сходство с первой фразой.
