#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! \n \n")
nr_letters= random.randint(3 , 6)
nr_symbols = random.randint(4, 8)
nr_numbers = random.randint(3 , 6)

password_list = []

for char in range(1 , nr_letters+1):
    password_list += random.choice(letters)

for char in range(1 , nr_symbols):
    password_list += random.choice(symbols)

for char in range(1 , nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print("👇 Here is your random password: \n ")
print(''.join(password_list))
