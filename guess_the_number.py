'''
The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements


Jumping off the first project, this project continues to build up the base knowledge and introduces user-inputted data at its very simplest. With user input, we start to get into a little bit of variability.
'''

import random

input_range = input('Range (Example, 0,100):')
# todo: check range_input is valid

# parse the input
input_a,input_b = input_range.split(',')

a = int(input_a)
b = int(input_b)

# generate a random number
random.seed = 20008 # set the seed so that results are repeatable
rand_num = random.randint(a,b)

print('A number to guess is generated!')
# ask to guess
max_guess_times = 3
succeeded = False
print('You have {} times to guess, good luck!'.format(max_guess_times))
for i in range(max_guess_times):
    input_guess = input('Your {0} guess:'.format(i+1))
    guess = int(input_guess)
    if guess == rand_num:
        print('Yeah!')
        succeeded = True
        break
    else:
        # give some hints
        hint = ''
        if guess > rand_num:
            hint = 'greater'
        else:
            hint = 'smaller'
        print('Your guess is {} than the number, please try again'.format(hint))

if succeeded:
    print('You win!')
else:
    print('Sorry failed!')
