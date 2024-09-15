## --------------------- Сєваті Євген КН-31\1
text = ("Whether you're travelling to the islands or the mountains of Thailand, " ## Створення тексту
         "you're likely to spend at least one night in its capital city on the way."
        " Bangkok might be noisy and polluted but it's also an exciting city with plenty of things to see and do. "
         "Why not make it a longer stay?")
print(text, "\n") ## Вивід тексту у консоль
print(text.lower(), "\n") ## Вивід тексту нижнім регістром букв
print("Amount of letter 'a' in text = ", text.count('a') + text.count('A'), "\n") ## Вивід кількість букв "а" у тексті
print("Is our text lowercased? ", text.islower(), "\n") ## Вивід чи написаний вхідний текст нижнім регістром букв

## --------------------- Лобанов Денис КН-33\1
print(text.replace(" ", "-"), "\n") ## Замінити всі пробіли на дефіси
print("Is our text alphabetic? ", text.isalpha(), "\n") ## Перевірка, чи текст складається лише з букв
print("First occurrence of 'city' is at index: ", text.find("city"), "\n") ## Знайти перше слово "city"

## --------------------- Віхтенко Данило КН-35
print(text.title(), "\n") # Перетворює першу літеру кожного слова в тексті на велику
print("Text starts with 'Whether'? ", text.startswith("Whether"), "\n") # Перевірка, чи починається текст зі слова "Whether"
print("Split text into words: ", text.split(), "\n") # Розділяє текст на список слів
## --------------------- Костюк Костянтин КН-33
print(text.count("city"), "\n") #Порахує, скільки разів зустрічається слово "city"
print("All lowercase:", text.lower(), "\n") #Перетворює увесь текст у нижній регістр
print("Does it start with 'Whether'?",text.startswith("Whether"), "\n") # Перевіряє, чи починається текст з "Whether"