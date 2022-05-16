# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

#print('DEBUG: Secret number is ' + str(secretNumber))

#6 guesses, range(1,7)
for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    #else, i.e. correct guess, break out of this loop.
    else:
        break 
    
if guess == secretNumber:
    print('\nGood job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else: 
    print('\nNope, the number I was thinking of was ' + str(secretNumber) + '!')