# 1 сложить числа

marks = [5, 5, 4, 5, 3, 3, 2, 5, 4]
marks_sum = 0
for mark in marks:
    marks_sum = marks_sum + mark # тут должно быть что-то с mark и marks_sum

print(marks_sum) # тут должно быть 36

# 2 часть
marks = {'2a': [5, 5, 4, 5, 3, 3, 2, 5, 4]}
marks_sum = 0

for mark in marks['2a']:
 marks_sum += mark
print(marks_sum)  # тут должно быть 36, сумма оценок 2а

# 3 часть
# сперва посмотри видео про словари, чтобы вспомнить, что делает метод items
# тут должно происходить что-то, что выводит класс и сумму его оценок
# В результате должно получиться такое:
# 2a 36
# 3b 19

marks = {
    '2a': [5, 5, 4, 5, 3, 3, 2, 5, 4], 
    '3b': [4, 5, 2, 5, 3]
    }


for class_name,class_marks in marks.items():
    
    marks_sum = 0
    for summ_marks in class_marks:
        marks_sum += summ_marks
    print(class_name,marks_sum)




marks = {
    '2a': [5, 5, 4, 5, 3, 3, 2, 5, 4], 
    '3b': [4, 5, 2, 5, 3]
    }


for class_name,class_marks in marks.items():
    a = sum(class_marks)
    print(class_name,a)
