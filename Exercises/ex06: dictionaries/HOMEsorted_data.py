# Arinell's:4
# Pancho Villa:3
# Andalu:3
# Urbun Burger:1
# El Toro:5
# Casa Thai:2
# Taqueria Cancun:2
# Little Baobab:1
# Charanga:3
# Irma's Pampanga:5
# Bay Blend Coffee and Tea:3
# Giordano Bros:2

text = open("scores.txt")
restaurant_list = []
restaurant_report = {}
score_list = []

for line in text:
	line.rstrip()
	restaurant, score = line.split(':')
	restaurant_list.append(restaurant)
	score_list.append(score)

print score_list
restaurant_list.sort()
print restaurant_list

for restaurant in restaurant_list:
	restaurant_report[restaurant] = 
	print "%s has a score of %d." % (restaurant, 