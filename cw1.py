print("Введіть число або текст")
text = input()
length = len(text)
print(length)

listed_text = list(text)
print(listed_text)

first_char = text[0]
last_char = text[-1]
print("перший символ:", first_char)
print("другий символ:", last_char)
substring = text[1:4]
print("символи з 2 по 4 символи:", substring)

print(text.upper())

text_with_underscores = text.replace(' ', '_')
print("текст з побілами замінені на нижні підкреслення:", text_with_underscores)

print("Введіть підрядок, щоб знайти його позицію: ")
search_substring = input()
position = text.find(search_substring)

if position != -1:
    print(f"Підрядок '{search_substring}' знаходиться на позиції: {position}")
else:
    print(f"Підрядок '{search_substring}' не знайдений в тексті.")