def number(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = split_even_odd(numbers)

print("Парні числа:", even)
print("Непарні числа:", odd)