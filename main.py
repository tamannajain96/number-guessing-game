#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
