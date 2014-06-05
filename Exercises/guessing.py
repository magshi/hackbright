# imports the library called random
import random

# prints a string to the console
print "Hello, person! What's your name?"

# ask the user for input in the form of a string
name = raw_input("> ")

# greet the user and prompt them to guess the number
print "Hello, %s" % name
print "I'm thinking of a number between 1 and 100. Try to guess my number!"

# generate a random number
comp_number = random.randrange(1, 101)

# set the count of tries to zero
count = 0

while True:
    usr_number = int(raw_input("Guess? "))
    count = count + 1
 
    if usr_number != comp_number:
        if usr_number < comp_number:
            print "Your guess is too low, try again"
        elif usr_number > comp_number:
            print "Your guess is too high, try again"
    else:
        print "Well done, %s! You found my number in %d tries!" % (name, count)
        break
