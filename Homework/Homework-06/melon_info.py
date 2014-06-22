"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melondex

def melon_report():
	for melon, value in melondex.iteritems():
		# this will print each melonkey in the dictionary with its value
		print "The average price of a %s is %s" % (melon.upper(), value)

def main():
	melon_report()

def print_melon(name, seedless, price):
	hashasnot = 'have'
	if seedless:
		hashasnot = 'do not have'
	
	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)

if __name__ == '__main__':
    for i in melondex.keys():
    	print i

if __name__ == '__main__':
	main()