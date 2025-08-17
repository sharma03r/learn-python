import random
player_choice = int(input("Enter your choice, 0 for rock, 1 for paper and 2 for scissors"))
if player_choice<0 or player_choice>2:
  print("Wrong input")
  raise SystemExit

computer_choice = random.randint(0,2)
choices = ["Rock", "Paper", "Scissors"]
print(f"You chose {choices[player_choice]}, Computer chose {choices[computer_choice]}")

if (player_choice - computer_choice) % 3 == 1:
  print("You won!")
elif (player_choice-computer_choice == 0):
  print("It's a draw!")
else:
  print("You lose!")
