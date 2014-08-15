string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	string_dict = {}
	word_list = string1.split()
	i = 0
	for item in word_list:
		string_dict[word_list[i]] = i
		i += 1
	print string_dict

# count_unique(string1)

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	return list(set(list1).intersection(list2))

common_items(list1, list2)

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	duplicate_dict = {}

	for value in list1:
		if duplicate_dict.get(value):
			duplicate_dict[value] = 1
		else:
			duplicate_dict[value] += 1
	for value in list2:
		if duplicate_dict.get(value):
			duplicate_dict[value] += 1
		else:
			duplicate_dict[value] = 1

	for key, value in duplicate_dict.iteritems():
		if len(value) > 1:
			print "The number '%d' appears %d times.\n" % (key, value)
	

# common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
	dictionary = {}
	for number in list1:
		dictionary[number] = number
	for number in list1:
		if dictionary.get(number*-1):
			print dictionary[number], number

# sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	dictionary = {}
	for word in words:
		dictionary[word] = word
	for word in words:
		if dictionary.get(word):
			print "The word %s is a duplicate with %s" % (word, dictionary.get(word))

# find_duplicates(words)

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    word_length_dict = {}
    list_of_lengths = []
    for word in words:
    	if len(word) in word_length_dict:
    		word_length_dict[len(word)].append(word)
    	else:
    		word_length_dict[len(word)] = [word]
    for k, v in word_length_dict.iteritems():
    	print k, v

    print list_of_lengths


word_length(words)

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentence translated to pirate.
"""

# see piratespeak.py