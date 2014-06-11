"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melondex

# from melons import melon_name, melon_seedless, melon_price

# melondex = {
#     "Honeydew": [0.99, True, 'orange', 'bumpy', 'melonheavy'],
#     "Crenshaw": [2.00, False, 'fleshcolor', 'rindcolor', 'weight'],
#     "Crane": [2.50, False, 'fleshcolor', 'rindcolor', 'weight'],
#     "Casaba": [2.50, False, 'fleshcolor', 'rindcolor', 'weight'],
#     "Cantaloupe": [0.99, False, 'fleshcolor', 'rindcolor', 'weight']
# }

def melon_report():
	for melon in melondex.keys():
		print "%s:\n" % melondex[melon]


# def print_melon(name, seedless, price):
# 	hashasnot = 'have'
# 	if seedless:
# 		hashasnot = 'do not have'
	
# 	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)

# if __name__ == '__main__':
#     for i in melon_name.keys():
#         print_melon(melon_name[i], melon_seedless[i], melon_price[i])

if __name__ == '__main__':
	melon_report()