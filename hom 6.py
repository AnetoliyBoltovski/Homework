
animals_fast = set(["cat", "turtle", "rabbit", "cheetah", "gazelle"])
animals_slow = set(["turtle", "snail", "sloth", "Mole", "Greenland polar shark"])

all_fur = animals_slow | animals_fast
print(all_fur)

intersection_fur = animals_slow & animals_fast
print(intersection_fur)

difference_fur = animals_slow ^ animals_fast
print(difference_fur)

check_fur = animals_slow.issubset(animals_fast)
print(check_fur)