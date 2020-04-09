#Password generator
import random
import string

def call_alphabets():
  print("How many alphabet characters do you want in your password: ")
  global character_alpha
  character_alpha=int(input())
  if character_alpha >= pass_length:
    print("Sorry the alphabet character are more than total lenght of your password please select a lower number than your total pass length ")
    call_alphabets()
  return character_alpha

def call_numbers():
  print("How many number characters do you want in your password: ")
  global character_number
  character_number=int(input())
  if character_number >= pass_length - character_alpha:
    print("Please select a lower number")
    call_numbers()
  return character_number

def pass_generator_alpha():
  i = 0
  random_string=""
  while i < character_alpha:
    random_string += random.choice(string.ascii_letters)
    i += 1
  return(str(random_string))
    
def pass_generator_number():
  i = 0
  random_string=""
  while i < character_number:
    random_string += str(random.randint(0,9))
    i += 1
  return(str(random_string))


print("How long do you want your password to be (total characters):")
pass_length=int(input())

call_alphabets()
call_numbers()

total_char = character_alpha + character_number
remain_char = pass_length - total_char

def pass_generator_special():
  special = ['~','!','@','#','$','%','^','&','*','(',')','-','+'] 
  i = 0
  random_string=""
  while i < remain_char:
    random_string += random.choices(special)[0]
    i += 1
  return(str(random_string))

print("Thank you. You have requested a password with " + str(character_alpha) + " alphabet characters and " + str(character_number) + " numbers characters and we will add " + str(remain_char) + " remaining as special characters ")

print("Your randomly generated password is below:")

finalpass = pass_generator_alpha()+pass_generator_number()+pass_generator_special()

finalpass_length = len(finalpass)

i = 0
final_string=""
while i < finalpass_length:
  final_string += random.choices(finalpass)[0]
  i += 1

print(final_string)
