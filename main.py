#Number Guessing Game Objectives:
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing game")
# Include an ASCII art logo.

#Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def compare (guess , num):
  if guess > num:
    print("Too High")
  elif guess < num:
    print("Too low")

numbers = []
for number in range (1,101):
  numbers.append(number)
num = random.choice(numbers)
print(f"I'm thinking of a number between 1 and 100 {num}")
difficulty_level = input("Choose a difficulty. Type 'easy or 'hard: ").lower()
no_of_attempts = 0
if difficulty_level == "easy":
  no_of_attempts = 10
  guess = 0
  while no_of_attempts != 0:
    print(f"You have {no_of_attempts} attempts remaining to guess the number")
    # Allow the player to submit a guess for a number between 1 and 100.
    guess = int(input("Make a Guess: "))
    if guess == num:
      print("You have guessed the answer")
      no_of_attempts = 0
    elif guess != num:
      compare (guess , num)
    # Track the number of turns remaining.
      no_of_attempts -= 1
elif difficulty_level == "hard":
  no_of_attempts = 5
  guess = 0
  while no_of_attempts != 0:
    print(f"You have {no_of_attempts} attempts remaining to guess the number")
    guess = int(input("Make a Guess: "))
  # If they got the answer correct, show the actual answer to the player.
    if guess == num:
      print("You have guessed the answer")
      no_of_attempts = 0
    # Track the number of turns remaining. 
    elif guess != num:
      compare (guess , num)
      no_of_attempts -= 1 
      if no_of_attempts == 0:
      # If they run out of turns, provide feedback to the player
        print("You've run out of guesses, You loose")
  
