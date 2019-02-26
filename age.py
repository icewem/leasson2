# Определить возраст, положив в переменную
# Исходя из возраста выдать сообщение как быть дальше

def age_group():
    age = int(input("Привет, введи свой возраст:"))
    if age >= 0 and age <= 6:
        return("Садик")
    if age >= 7 and age <= 17:
        return("Школа")
    if age >= 18 and age <= 23:
        return("Университет")
    return("Работа")

result = age_group()
print(result)