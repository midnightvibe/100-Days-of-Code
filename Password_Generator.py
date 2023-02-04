#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


pw_list= []
for letter in range(1, nr_letters + 1):
    # pw_list += [letters[random.randint(0, len(letters) - 1)]]
    pw_list += [random.choice(letters)]

pw_symbols = []
for symbol in range(1, nr_symbols + 1):
    # pw_list += [symbols[random.randint(0, len(symbols) - 1)]]
    pw_list += [random.choice(symbols)]

pw_numbers = []
for number in range(1, nr_numbers + 1):
    # pw_list += [numbers[random.randint(0, len(numbers) - 1)]]
    pw_list += [random.choice(numbers)]

password_randomized = []
for entry in range(1, len(pw_list) + 1):
    n = random.randint(0, len(pw_list) - 1)
    password_randomized += [pw_list[n]]
    pw_list.pop(n)

password = ""
for char in range(1, len(password_randomized) + 1):
    password += password_randomized[char-1]
print(password)
