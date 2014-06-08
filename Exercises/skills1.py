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
    print word_list

long_words(['hello', 'engine', 'yard', 'rails girls', 'tomato', 'quaker', 'sriracha', 'bean sprouts', 'beachball', 'killer whale', 'frontier', 'wagonface'])

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return None

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return []

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return []

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None