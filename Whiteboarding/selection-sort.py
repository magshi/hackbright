# SELECTION SORT
# O(n^2)

def selection_sort(list):
	for fill_slot in range(len(list)-1, 0, -1):
		max_position = 0
		for location in range(1, fill_slot+1):
			if list[location] > list[max_position]:
				max_position = location

		temp = list[fill_slot]
		list[fill_slot] = list[max_position]
		list[max_position] = temp

	print list

def main():
	list = [5, 1, 4, 23, 5, 0, 3, 3, 8, 2, 8]
	selection_sort(list)