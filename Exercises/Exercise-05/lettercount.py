from sys import argv
from os.path import exists

def count_letters(filename):
    letter_tally = [0]*26

    print letter_tally
    print len(letter_tally)

    text = open(filename)
    print text

    for line in text:
        words = line.split()
        print words

    # text = open(filename).read()

    # for character in text:
    #   letter_tally[ord(character) - 97] += 1
    # print letter_tally

def main():    
    count_letters("essay-on-criticism.txt")

if __name__ == "__main__":
    main()