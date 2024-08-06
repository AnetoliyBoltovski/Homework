def calculator():
    try:
        
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))


        operation = input("Виберіть операцію (+, -, *, /): ")


        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Помилка: ділення на нуль!")
                return
        else:
            print("Помилка: некоректна операція!")
            return


        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: некоректне введення!")


calculator()