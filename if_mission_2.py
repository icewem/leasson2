# Практика: Сравнение строк
#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты


def two_line(line_one,line_two):
    if not isinstance(line_one,str) and not isinstance(line_two,str):  # isinstance проверяет принадлежат ли данные к нужному типу, можно проверить принадлежит ли к одному из нескольких типов.
        return("0")
    elif line_one == line_two:
        return("1")
    elif line_one != line_two and line_one > line_two:
        return("2")
    elif line_one != line_two and line_two == "learn":
        return("3")

go_compare = two_line(input("Введите первую строку:"),input('Введите вторую строку:'))
print(go_compare)