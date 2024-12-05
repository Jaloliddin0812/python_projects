
gi


import random
print("Hello\nWhat do you choose Type 0 for Rock, 1 for Paper or 2 for scissors" )
your_choice = int(input())

if your_choice == 0:
  print('''888
                       888
                       888
888d888 .d88b.  .d8888b888  888
888P"  d88""88bd88P"   888 .88P
888    888  888888     888888K
888    Y88..88PY88b.   888 "88b
888     "Y88P"  "Y8888P888  888 ''')

elif your_choice ==1:
  print(''' _ __   __ _ _ __   ___ _ __
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |
| .__/ \__,_| .__/ \___|_|
| |         | |
|_|         |_| ''')
elif your_choice == 2:
  print('''   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.''')
else:
  print("Invalid")

items = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(0,2)
print(f"Computer chose {items[computer_choice]}")

if your_choice == computer_choice:
  print("Draw")
elif your_choice == 0 and computer_choice == 1 or your_choice == 1 and computer_choice == 2 or your_choice == 2 and computer_choice ==0:
  print("Computer won the game")
else:
  print("Congratulations\nYou won the game")
