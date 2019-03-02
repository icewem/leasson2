def cut_cake(parts):
    try:
        return 1 / int(parts)
    except ZeroDivisionError:
        return 'зачем делить на ноль?'
    except TypeError:
        return 'ошибка типа'
    except ValueError:
        return 'ошибка значения'
cake = cut_cake("?")
print(cake)