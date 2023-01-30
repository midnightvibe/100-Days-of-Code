import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_payee = random.randint(0, len(names))

print(f"{names[num_payee]} is going to buy the meal today!")
