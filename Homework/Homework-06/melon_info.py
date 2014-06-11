"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melondex

# from melons import melon_name, melon_seedless, melon_price

def melon_report():
	for melon, value in melondex.iteritems():
		print melon, value

def main():
	melon_report()

# def print_melon(name, seedless, price):
# 	hashasnot = 'have'
# 	if seedless:
# 		hashasnot = 'do not have'
	
# 	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)

# if __name__ == '__main__':
#     for i in melon_name.keys():
#         print_melon(melon_name[i], melon_seedless[i], melon_price[i])

if __name__ == '__main__':
	main()