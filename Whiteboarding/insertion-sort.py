# INSERTION SORT
# O(n^2)

def insertion_sort(list):
	for index in range(1, len(list)):
		current_value = list[index]
		position = index

		while position > 0 and list[position - 1] > current_value:
			list[position] = list[position - 1]
			position = position - 1

		list[position] = current_value

	print list

def main():
	list = [5, 1, 4, 23, 0, 2, 8]
	insertion_sort(list)