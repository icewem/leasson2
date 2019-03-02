def cut_cake(parts):
    try:
        return 1 / int(parts)
    except (ZeroDivisionError,TypeError,ValueError):
        return 'зачем делить на ноль?'

cake = cut_cake("dfdfdf")
print(cake)