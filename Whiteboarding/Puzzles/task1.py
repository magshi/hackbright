#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

def reverse_sort(l):
	# print l
	for i in range(len(l)/2):
		j = -1 - i
		temp = l[i]
		l[i] = l[j]
		l[j] = temp
	print l

reverse_sort(l)