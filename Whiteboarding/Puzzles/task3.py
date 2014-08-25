#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 93, 10, 66]
l2 = [93, 2, 3, 6, 23, 77, 66]

def remove_duplicates(l1, l2):
	duplicates_dict = {}
	l3 = []

	for item in l1:
		if item in duplicates_dict:
			duplicates_dict[item] += 1
		else:
			duplicates_dict[item] = 1
			
	for item in l2:
		if item in duplicates_dict:
			duplicates_dict[item] += 1
		else:
			duplicates_dict[item] = 1

	for item, occurrences in duplicates_dict.iteritems():
		if duplicates_dict[item] == 1:
			l3.append(item)

	print l3

remove_duplicates(l1, l2)