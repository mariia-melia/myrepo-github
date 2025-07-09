# Отримуємо строку від користувача
text = input("Введи текст, який має містити строго не менше 10 унікальних символів: ")

# Рахуємо унікальні символи
unique_chars = []

for char in text:
    if char not in unique_chars:
        unique_chars.append(char)

# Перевіряємо кількість унікальних символів
if len(unique_chars) > 10:
    print(True)
else:
    print(False)