# 1-5 Guess the number

import random

x = 100

a =  random.randrange(1,x,1)
# a = random.choice(range(1,101))
#print("Guess the random integer between 1 and " + str(x) + ". Q exits.")
print(f"Guess the random integer between 1 and {x}. \'Q\' exits")
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
    

# Using try/except yields a slightly shorter, slightly neater
# program:

# import random

# secret_number = random.choice(range(101))

# guess_counter = 0

# while True:
#     guess = input("Enter a number or type \'q\' to quit\t")
#     print(guess)
#     if guess == 'q':
#         break
#     else:
#         try:
#             my_guess = int(guess)
#             guess_counter += 1
#         except:
#             print("That's not an Integer! (Whole Number)")
#             continue
    
#     if my_guess == secret_number:
#         print("You Win!")
#         print("It took {0} guesses".format(guess_counter))
#         break
#     elif my_guess < secret_number:
#         print("Too low... Try a larger number")
#     elif my_guess > secret_number:
#         print("Too high... Try a smaller number")