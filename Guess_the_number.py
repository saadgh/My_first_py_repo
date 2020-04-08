import random

random_number = random.randrange(0,20)

print(random_number)
print("The computer has generated a number between 0 to 20. Can you guess what is the number?")
user_input = int(input())

if random_number == user_input:
  print("You guessed it right, the number is " + str(random_number))
elif random_number > user_input:
  print("Computer's number is bigger than yours")
else:
  print("Your number is bigger than computer's")
