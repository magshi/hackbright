# BUBBLE SORT
# O(n^2)

def bubble_sort(list):
	for pass_num in range(len(list)-1, 0, -1):
		for i in range(pass_num):
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp
	print list

def main():
	list = [5, 1, 4, 23, 0, 2, 8]
	bubble_sort(list)