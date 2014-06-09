# # Things you should be able to do.

# # Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
	list_of_odds = []
	for value in some_list:
		if int(value) % 2 != 0:
			list_of_odds += [value]
	print list_of_odds

# all_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# # Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
	list_of_evens = []
	for value in some_list:
		if int(value) % 2 == 0:
			list_of_evens += [value]
	print list_of_evens

# all_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# # Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
	long_word_list = []
	for word in word_list:
		if len(word) >= 4:
			long_word_list += [word]

	print long_word_list

# long_words(['hey', 'bot', 'yard', 'rails girls', 'tomato', 'quaker', 'sriracha', 'hot', 'uh', 'bean sprouts', 'beachball', 'killer whale', 'cat', 'wagonface'])

# # Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
	lowest_value = some_list[0]

	for value in some_list:
		if value < lowest_value:
			lowest_value = value
	print "The smallest integer in %r is %d." % (some_list, lowest_value)

# smallest([800, 34, 750, 500, 347, 1946, 40, 1988, 55])

# # Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# # Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
# # how to use floats in this if the number is odd?!
def halvesies(some_list):
	list_of_halves = []
	for number in some_list:
		
		list_of_halves += [float(number / 2.0)]
	print list_of_halves

halvesies([3, 6, 9, 12, 18, 24, 32, 48, 51, 96, 1988, 1946, 1951, 1984])

# # Write a function that takes a list of words and returns a list of all the lengths of those words.
# def word_lengths(word_list):
#     length_list = []
#     for word in word_list:
#     	length_list += [len(word)]
#     	print "%s is %d characters long." % (word, len(word))

# word_lengths(['elephant', 'tiger', 'hemingway', 'wallace', 'costeau', 'camus', 'kierkegaard', 'kundera'])

# # Write a function (using iteration) that sums all the numbers in a list.
# def sum_numbers(numbers):
#     sum_of_list = 0
#     for value in numbers:
#     	sum_of_list += value
#     print "The sum of the numbers you gave me is %d." % sum_of_list

# sum_numbers([5, 5, 5, 5, 5, 10, 10, 5, 30, 1, 1, 1, 2, 15])

# # Write a function that multiplies all the numbers in a list together.
# def mult_numbers(numbers):
# 	product = 1
# 	for value in numbers:
# 		product *= value
# 	print "The product of the numbers you gave me is %d." % product

# mult_numbers([2, 4, 6, 8, 10])

# extra challenge: write a function that takes a string from a text file and breaks up every word into a separate string, then makes a list of all those strings :)

def disjoin_strings(text):
	text = open("tmrw-and-tmrw-and-tmrw.txt")
	big_list_of_strings = []
	for line in text:
		word = line.split()
		big_list_of_strings += word
	return big_list_of_strings

# string_list = disjoin_strings("tmrw-and-tmrw-and-tmrw.txt")

# # Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(list_of_strings):
	print "I'm working!!!"
	print list_of_strings

	combined_string = ''
	for item in list_of_strings:
		combined_string += item + " "

	print combined_string

# join_strings(string_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    added_up = 0

    for i in numbers:
    	added_up += i
    	print added_up

    average = added_up / len(numbers)
    print "The average of %r is %r." % (numbers, average)

# average([2, 4, 6, 8])
# average([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])