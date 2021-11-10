import random

guess1 = input("Guess the number from 1-10: ")

guess1 = int(guess1)

answer = random.randint(1,10)

if guess1 == answer:
  print("Correct!")
  quit()

if guess1 > answer:
  print("Lower")

if guess1 < answer:
  print("Higher")

guess2 = input("Try again: ")

guess2 = int(guess2)

if guess2 == answer:
  print("Correct!")
  quit()

if guess2 > answer:
  print("Lower")

if guess2 < answer:
  print("Higher")

guess3 = input("Last chance, try again: ")

guess3 = int(guess3)

if guess3 == answer:
  print("Correct!")
  quit()
else:
  print("The correct number was " + str(answer))
