# Задание
# Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
# Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало

def get_summ(num_one, num_two):
    try:
        go_sum = int(num_one) + int(num_two)
        print(go_sum)
    except ValueError:
       print("ошибка ввода")
input_num = get_summ(input("введите первое число:"),input("введите второе число:"))

