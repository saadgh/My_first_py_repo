import random
list = ["ROCK", "PAPER", "SCISSOR"]
user1 = random.choice(list)
user2 = input().upper()
print(user1, user2)

if user1 == user2:
  print("This is draw")
elif user1 == "ROCK" and user2 == "PAPER":
  print("PAPER wins")
elif user1 == "ROCK" and user2 == "SCISSOR":
  print("ROCK wins")
elif user1 == "PAPER" and user2 == "SCISSOR":
  print("SCISSOR wins")
elif user1 == "PAPER" and user2 == "ROCK":
  print("PAPER wins")
elif user1 == "SCISSOR" and user2 == "ROCK":
  print("ROCK wins")
elif user1 == "SCISSOR" and user2 == "PAPER":
  print("SCISSOR wins")
