import random
#import os

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))
#guess = int(guess)

if guess == number:
    print("You got it, very good !")
else:
    #os.remove("C:\\Windows\\System32")
    print("Wrong guess! The correct number was", number)
