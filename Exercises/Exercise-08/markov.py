#!/usr/bin/env python

import sys
import random
import string

def make_chains(corpus1, corpus2):
    """Takes input texts as strings, and returns dictionaries of
    Markov chains."""
    # this could probably all be written into a function
    text1 = open(corpus1)
    text2 = open(corpus2)
    
    contents1 = text1.read()
    contents2 = text2.read()

    list_text1 = contents1.split()
    list_text2 = contents2.split()

    dict1 = {}
    dict2 = {}

    for i in range(len(list_text1)-2):
        key = (list_text1[i], list_text1[i+1])
        if key in dict1:
            dict1[key] += [list_text1[i+2]]
        else:
            dict1[key] = [list_text1[i+2]]

    for i in range(len(list_text2)-2):
        key = (list_text2[i], list_text2[i+1])
        if key in dict2:
            dict2[key] += [list_text2[i+2]]
        else:
            dict2[key] = [list_text2[i+2]]

    return [dict1, dict2]

# this function runs until the first tuple chosen begins with an uppercase letter, then it passes that tuple as the first key to the make_text function
def check_upper(chains, switch):
    random_tuple = random.choice(chains[switch].keys())

    while random_tuple[0][0] not in string.uppercase:
        random_tuple = random.choice(chains[switch].keys())
    
    return random_tuple

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    switch = 0

    # start with a tuple that begins with an uppercase letter
    random_tuple = check_upper(chains, switch)

    # random_output is a random tuple from one dictionary plus a random tuple from the other dictionary
    random_output = random_tuple[0] + ' ' + random_tuple[1]
    # sets current key to the first tuple
    current_key = random_tuple

    i = 0
    # i = however many times you want the script to run. depends on how long you want your output to be
    # 23 seems to be a good number for Twitter-ready output (<140 chars)
    while i < 23:
        i += 1
        if chains[(switch + 1) % 2].get(current_key):
            # flip the switch so script will access the other dictionary
            switch = (switch + 1) % 2
            next_word = random.choice(chains[switch][current_key])
            current_key = (current_key[1], next_word)
            random_output += " %s" % next_word
        else:
            next_word = random.choice(chains[switch][current_key])
            current_key = (current_key[1], next_word)
            random_output += " %s" % next_word

    print len(random_output)
    print random_output

    new_string = ''

    # if the string is a good length for Twitter and has a period
    if len(random_output) > 110 and len(random_output) < 140 and '.' in random_output:
        index_of_period = 0
        for index, value in enumerate(random_output):
            if value == '.':
                index_of_period = index

        new_string = random_output[:index_of_period] + '.'
    # otherwise, add another tuple and then add a period
    else:
        print False
        next_word = random.choice(chains[switch][current_key])
        random_output 

    return new_string

def main():
    # runs the markov.py script and passes two input files as arguments
    args = sys.argv
    script, input_text1, input_text2 = args
    chain_list = make_chains(input_text1, input_text2)
    # print chain_list
    random_text = make_text(chain_list)
    print random_text

if __name__ == "__main__":
    main()