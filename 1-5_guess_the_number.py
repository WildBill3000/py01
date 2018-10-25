# 1-5 Guess the number

import random

x = 100

a =  random.randrange(1,x,1)
print("Guess the random integer between 1 and " + str(x) + ". Q exits.")
i = 0
while True:
    while True:
        guess = input("Your guess? ")
        if guess.upper() == 'Q':
            break
        elif guess.isnumeric():
            break
        else:
            print("That\'s not a very good guess.")
    if guess.upper() == 'Q':
        print("You are no fun.")
        break
    i += 1
    guess = int(guess)
    if guess < a:
       print("Higher.")
    elif guess > a:
        print("Lower.")
    elif guess == a:
        print("Congratulations. You guessed the number in " + str(i) + " tries.")
        break
    else:
        print("Huh?")
    