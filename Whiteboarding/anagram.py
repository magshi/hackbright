def is_anagram(string1, string2):
	count1 = [0]*26
	count2 = [0]*26

	for i in range(len(string1)):
		pos = ord(string1[i]) - ord('a')
		count1[pos] += 1

	for i in range(len(string2)):
		pos = ord(string2[i]) - ord('a')
		count2[pos] += 1

	j = 0
	stillOK = True

	while j < 26 and stillOK:
		if count1[j] == count2[j]:
			j += 1
		else:
			stillOK = False

	# print count1
	# print count2
	print stillOK

is_anagram('heart', 'earth')