print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
direction = input("Choose your direction: left or right?")
if direction=="right":
  print("Game Over.")
  exit(0)
action = input("Do you want to swim or wait?")
if action == "swim":
  print("Game Over")
  exit()
door = input("Choose your door: Red, Blue or Yellow")
if door == "Yellow":
  print("You Win.")
else:
  print("Game Over")