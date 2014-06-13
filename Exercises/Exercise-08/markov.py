#!/usr/bin/env python

import sys
import random
import string

def make_chains(corpus1, corpus2):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
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

def check_upper(chains, switch):
    random_tuple = random.choice(chains[switch].keys())

    while random_tuple[0][0] not in string.uppercase:
        random_tuple = random.choice(chains[switch].keys())
    
    return random_tuple

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    switch = 0

    random_tuple = check_upper(chains, switch)

    random_output = random_tuple[0] + ' ' + random_tuple[1]
    current_key = random_tuple

    i = 0

    while i < 30:
        i += 1
        if chains[(switch + 1) % 2].get(current_key):
            switch = (switch + 1) % 2
            next_word = random.choice(chains[switch][current_key])
            current_key = (current_key[1], next_word)
            random_output += " %s" % next_word
        else:
            next_word = random.choice(chains[switch][current_key])
            current_key = (current_key[1], next_word)
            random_output += " %s" % next_word

    return random_output

def main():
    args = sys.argv
    script, input_text1, input_text2 = args
    chain_list = make_chains(input_text1, input_text2)
    random_text = make_text(chain_list)
    print random_text

if __name__ == "__main__":
    main()