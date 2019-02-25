def age_group(age):
    if age >= 3 and age <= 6:
        return("Садик")
    elif age >= 7 and age <= 17:
        return("Школа")
    elif age >= 18 and age <= 23:
        return("Университет")
    elif age >= 24 and age <= 99:
        return("Работа")

result = age_group(int(input("Привет, введи свой возраст:")))
print(result)