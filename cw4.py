def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('помилка ділеться на 0')
    except TypeError:
        print('це не число')
        return
    else:
        return result
print(divide(8,4))