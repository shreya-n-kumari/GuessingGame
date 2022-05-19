import random 
import time

guess = 0

tries = 0

number = random.randint(1,10)

name = input("Howdy, May I Know Your Name? ")
print("Hello "+name+".")

question = input("Are You Ready To Guess? [Y/N] ")
time.sleep(1)						#to make the execution little bit slower intentionally.

if question.lower() == 'n':
    time.sleep(1)
    print("I'm sorry, We'll meet each other next time!")
    exit()
if question.lower() == 'y':
    time.sleep(1)
    print("I'm thinking of a number between 1 & 10")


while not (guess == number):
    time.sleep(1)
    guess = int(input("What's your guess? "))
    tries = tries + 1
    if guess == number:
        print("Brilliant")
        time.sleep(1)
        print("Congrats, Your Guess was correct. The number was indeed {}.".format(number))
        time.sleep(1)
        print("It has taken you {} tries".format(tries))
    elif guess < number:
        print("No! Guess Higher")
    elif guess > number:
        print("No! Guess Lower")



