# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.
'''
list_str = {"1","3","5","7","9","11","13","15","17","19"}
for go_screen in list_str:
    go_screen = int(go_screen) + 1  
    print(go_screen)

# сложить числа

list_str = {"1","3","5","7","9","11","13","15","17","19"}
for go_screen in list_str:
    go_screen = int(go_screen) + int(go_screen)  
    print(go_screen)

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

input_str = input("Приветствую.Введите строку, будет фокус:")

for go_down in input_str:
    print(go_down)

'''

# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

shool_perfomance = [
    {'school_class': '1a', 
    'scores': [3,4,4,5,2]},
    {'school_class': '1b', 
    'scores': [3,4,4,5,4,4,2,3,5,5,4,3]},
    {'school_class': '2a', 
    'scores': [5,3,5,4,3,3,5,4]},
    {'school_class': '2b', 
    'scores': [2,3,5,5,5,2]},
    {'school_class': '3a', 
    'scores': [5,4,4,2,3,5,4,5,2]},
    {'school_class': '4a', 
    'scores': [3,4,5,5,4,3]},
    {'school_class': '5b', 
    'scores': [5,5,4,3,5,2,4,5,2]}]

for shool_param in shool_perfomance:
    print(shool_param)



'''

scool = {'school_class': '1a', 'scores': [3, 4, 4, 5, 2]}
result = 0
fot test in scool['scores']:
    result += test
print(a)


marks = {
    '2a': [5, 5, 4, 5, 3, 3, 2, 5, 4], 
    '3b': [4, 5, 2, 5, 3]
    }


for class_name,class_marks in marks.items():
    
    marks_sum = 0
    for summ_marks in class_marks:
        marks_sum += summ_marks
    print(class_name,marks_sum)
'''