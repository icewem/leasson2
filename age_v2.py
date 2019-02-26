def age_group(age):
    if age >= 0 and age <= 6:
        return("Садик")
    if age >= 7 and age <= 17:
        return("Школа")
    if age >= 18 and age <= 23:
        return("Университет")
    return("Работа")

result = age_group(int(input("Привет, введи свой возраст:")))
print(result)