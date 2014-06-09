# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
	list_of_odds = []
	for value in some_list:
		if int(value) % 2 != 0:
			list_of_odds += [value]
	print list_of_odds

all_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
	list_of_evens = []
	for value in some_list:
		if int(value) % 2 == 0:
			list_of_evens += [value]
	print list_of_evens

all_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
	long_word_list = []
	for word in word_list:
		if len(word) >= 4:
			long_word_list += [word]

	print long_word_list

long_words(['hey', 'bot', 'yard', 'rails girls', 'tomato', 'quaker', 'sriracha', 'hot', 'uh', 'bean sprouts', 'beachball', 'killer whale', 'cat', 'wagonface'])

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return None

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
# how to use floats in this if the number is odd?!
def halvesies(some_list):
	list_of_halves = []
	for number in some_list:
		list_of_halves += [number / 2]
	print list_of_halves

halvesies([3, 6, 9, 12, 18, 24, 32, 48, 51, 96, 1988, 1946, 1951, 1984])

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []
    for word in word_list:
    	length_list += [len(word)]
    	print "%s is %d characters long." % (word, len(word))

word_lengths(['elephant', 'tiger', 'hemingway', 'wallace', 'costeau', 'camus', 'kierkegaard', 'kundera'])

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum_of_list = 0
    for value in numbers:
    	sum_of_list += value
    print "The sum of the numbers you gave me is %d." % sum_of_list

sum_numbers([5, 5, 5, 5, 5, 10, 10, 5, 30, 1, 1, 1, 2, 15])

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
	product = 1
	for value in numbers:
		product *= value
	print "The product of the numbers you gave me is %d." % product

mult_numbers([2, 4, 6, 8, 10])

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
	combined_string = ''
	for i in string_list:
		combined_string += i + " "
    return combined_string

join_strings("She should have died hereafter;
There would have been a time for such a word.
Tomorrow, and tomorrow, and tomorrow,
Creeps in this petty pace from day to day,
To the last syllable of recorded time;
And all our yesterdays have lighted fools
The way to dusty death. Out, out, brief candle!
Life's but a walking shadow, a poor player
That struts and frets his hour upon the stage
And then is heard no more. It is a tale
Told by an idiot, full of sound and fury
Signifying nothing.")

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None