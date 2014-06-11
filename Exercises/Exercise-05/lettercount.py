from sys import argv
from os.path import exists
import string

def count_letters(filename):

    letter_tally = [0]*26

    contents = open(filename).read()

    for line in contents:
        line = line.rstrip() # remove extra chars
        line = line.lower() # lowercase everything

        for char in line:
            if ord(str(char)) >= 97 and ord(str(char)) <= 122:
                letter_tally[ord(str(char)) - 97] += 1
            else:
                pass

    i = 0

    while i < 26:
        print string.ascii_lowercase[i], letter_tally[i]
        i += 1

def main():    
    count_letters("essay-on-criticism.txt")

if __name__ == "__main__":
    main()