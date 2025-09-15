import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword Generator!!")

nr_letters = int(input("How many letters would you like to have in password"))
nr_symbol = int((input (f"how many symbols would you like\n")))
nr_numbers = int(input(f"How many numbers would you like \n"))


password = []

for chars in range(1,nr_letters+1):
  password.append(random.choice(letters))
for char in range(1, nr_symbol+1):
 password+= random.choice(symbols)
for char in range(1 , nr_numbers+1):
  password+=random.choice(numbers)
print(password)
random.shuffle(password)
print(password)

password = ""
for char in password:
  password+= char
print(f"your password is : {password}")
