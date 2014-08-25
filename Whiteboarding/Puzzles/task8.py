#!/bin/env python

"""
Given two dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys
eg:
    d1 = {"a":1, "b":2}
    d2 = {"a":3, "c":4}

    becomes

    d1 = {"a":3, "b":2, "c":4}
"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

def overwrite_dict(d1, d2):
	for d2_key, d2_value in d2.iteritems():
		if d2_key in d1:
			print "Overwriting %r with %r for key %r" % (d1[d2_key], d2_value, d2_key)
			d1[d2_key] = d2_value

overwrite_dict(d1, d2)