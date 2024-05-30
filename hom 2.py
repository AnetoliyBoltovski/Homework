print("ведіть 3 любі цифри")

number1 = input("задайте значення 1 => ")
number2 = input("задайте значення 2 => ")
number3 = input("задайте значення 3 => ")

max_number = number1

    if number2 > max_number:
        max_number = number2
    if number3 > max_number:
        max_number = number3
    print(f"найбільше число {max_number}")