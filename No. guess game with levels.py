# Guess the number game by SIR. ADARSH ~

import random
from pyfiglet import figlet_format , Figlet
from termcolor import colored

print((colored(figlet_format(" SIR. ADARSH "), color="green")))
print('')
Name = input('Hello! What is your name? ')
print('1 = EASY')
print("2 = MEDIUM")
print("3 = HARD")
lvl = int(input('Pick a level of difficulty (1 to 3): ')) 
print('')
# change range and number of allowed guesses with level.....

if lvl == 1:
    print((colored(figlet_format(" EASY ",font='cyberlarge'), color="green")))
    print("-------- ONLY 10 TRIES YOU WILL GET AND A FREE TRIAL ;) ------")
    top = 100
    tries = 10
elif lvl == 2:
    print((colored(figlet_format(" MEDIUM ",font='cyberlarge'), color="green")))
    print("----- ONLY 15 TRIES YOU WILL GET AND A FREE TRIAL ;) -----")
    top = 500
    tries = 15
elif lvl==3:
    print((colored(figlet_format(" HARD ",font='cyberlarge'), color="green")))
    print("-------- ONLY 20 TRIES YOU WILL GET AND A FREE TRIAL ;) ----------")
    top = 1000
    tries = 20

# create a '%s = string' & '%d = numbers' formatted string....

sf = "Well, %s, I am thinking of a number between 1 and %d" 
print(sf % (Name, top))

# picking up the random integer...
num = random.randint(1, top)

print('Try to guess it!.')
print('')

guessesTaken = 0
print('TRIAL ATTEMPT : ')
while guessesTaken <= tries:
    guess = int(input('Take a guess: '))
    print('')
    guessesTaken += 1
    print("ATTEMPT : ",guessesTaken-1)
    if guess < num:
        print('Your guess is too low.') 
        print('')
        print("-------------------------------------") 
        print('')   
    if guess > num:
        print('Your guess is too high.')
        print('')
        print("-------------------------------------")
        print('')
    if guess == num:
        print('CORRECT GUESS! AND THE NUMBER WAS = ',guess)
        print((colored(figlet_format(" CONGRATS ",font='cyberlarge'), color="green")))
        break

if guess == num:
    sf = "Good job, %s! You guessed my number with %d guesses!"
    print(sf % (Name, guessesTaken-1))

if guess != num:
    num = str(num)
    print('Nope. The number was = ' + num)
    print((colored(figlet_format(" BYE-BYE ",font='cyberlarge'), color="green")))