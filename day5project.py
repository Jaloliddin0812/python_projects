import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!", '@', "#", "$", "%", "^", "&", "*", "(", ")"]

print("welcome to the PyPassword Generator")
print("How many letters do you want in your password")
nr_letters = int(input())
print("How many numbers do you want in you password")
nr_numbers = int(input())
print("how many symbols do you want in your passwords")
nr_symbols = int(input())

password = []

for char in range(1, nr_letters + 1):
  password += random.choice(letters)
for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
random.shuffle(password)
print(password)