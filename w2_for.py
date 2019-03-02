# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

list_str = ["1","3","5","7","9","11","13","15","17","19"]
for go_screen in list_str:
    go_screen = int(go_screen) + 1  
    print(go_screen)

# сложить числа

list_str = ["1","3","5","7","9","11","13","15","17","19"]
summ_list = 0
for go_screen in list_str:
    summ_list += int(go_screen)
print(summ_list)

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

input_str = input("Приветствую.Введите строку, будет фокус:")

for go_down in input_str:
    print(go_down)

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
all_score = 0
all_student = 0
for shool_param in shool_perfomance:
    class_crores = shool_param['scores']
    class_name = shool_param['school_class']
    marks_sum = 0
    middle_class = len(class_crores)
    for summ_class in class_crores:
        marks_sum += summ_class
    delta_class = marks_sum / middle_class
    print('Класс: {} имеет средний балл:{}'.format(class_name,delta_class))
    all_score += marks_sum
    all_student += middle_class
summ_shool = all_score / all_student
print('Средний балл по школе равен {}'.format(summ_shool))
