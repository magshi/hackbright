import random
# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(list = random.sample(range(100), 10)):
  new_list = []
  for value in list:
    if value % 2 != 0:
      new_list.append(value)
  print new_list

all_odd()

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(list = random.sample(range(100), 10)):
    new_list = []
    for value in list:
      if value % 2 == 0:
        new_list.append(value)
    print new_list

all_even()

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(list = ['dirty beaches', 'dog', 'casanova', 'boards of canada', 'cut', 'surfer pondscum', 'chai spice granola', 'montauk', 'kate winslet', 'daria', 'whitehall lane', 'masonry', 'pod', 'peanuts', 'oat', 'if']):
    new_list = []
    for word in list:
      if len(word) >= 4:
        new_list.append(word)
    print new_list

long_words()

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(list = random.sample(range(100), 10)):
    list = sorted(list)
    print list[0]

smallest()

# Write a function that finds the largest element in a list of integers and returns it.
def largest(list = random.sample(range(100), 10)):
    list = sorted(list)
    print list[-1]

largest()

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(list = random.sample(range(100), 10)):
    print list
    new_list = []
    for value in list:
      new_list.append(value/2)
    print new_list

halvesies()

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(list = ['dirty beaches', 'dog', 'casanova', 'boards of canada', 'cut', 'surfer pondscum', 'chai spice granola', 'montauk', 'kate winslet', 'daria', 'whitehall lane', 'masonry', 'pod', 'peanuts', 'oat', 'if']):
    length_list = []
    for word in list:
      length_list.append(len(word))
    print length_list

word_lengths()

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(list = random.sample(range(100), 10)):
    sum = 0
    for value in list:
      sum += value
    print sum

sum_numbers()

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(list = random.sample(range(100), 10)):
    product = 1
    for value in list:
      product *= value
    print product

mult_numbers()

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(list = ['dirty beaches', 'dog', 'casanova', 'boards of canada', 'cut', 'surfer pondscum', 'chai spice granola', 'montauk', 'kate winslet', 'daria', 'whitehall lane', 'masonry', 'pod', 'peanuts', 'oat', 'if']):
    big_ol_string = ''
    for word in list:
      big_ol_string += word
    print big_ol_string

join_strings()

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(list = random.sample(range(100), 10)):
    total = 0
    for value in list:
      total += value
    average = total/len(list)
    print average

average()
