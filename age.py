# Определить возраст, положив в переменную
# Исходя из возраста выдать сообщение как быть дальше

def age_group():
    age = int(input("Привет, введи свой возраст:"))
    if age >= 3 and age <= 6:
        return("Садик")
    elif age >= 7 and age <= 17:
        return("Школа")
    elif age >= 18 and age <= 23:
        return("Университет")
    elif age >= 24 and age <= 99:
        return("Работа")

result = age_group()
print(result)