"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentence translated to pirate.
"""

def build_dictionary(file):
	file = open("english_pirate.txt")
	contents = file.read().split('\n')
	english_pirate_dict = {}

	for item in contents:
		key_value_list = item.split(',')
		english_pirate_dict[key_value_list[0]] = key_value_list[1]
	return english_pirate_dict

def translate(English_sentence, dictionary):
	English_words = English_sentence.split()
	Pirate_words = []
	punctuation_chars = [',', '.', '?', '!']
	for word in English_words:

		# for an exact match, just append it to the output list
		if dictionary.get(word):
			# print "MATCH: '%s' is a key" % word
			Pirate_words.append(dictionary[word])

		# if there's a mismatch because of capitalization
		elif dictionary.get(word.lower()):
			new_word = dictionary.get(word.lower())
			Pirate_words.append(new_word.title()) # the title() method puts a string back in Title case

		# if there's a mismatch because of trailing punctuation (will NOT work on leading punctuation)
		elif dictionary.get(word[:-1]):
			if word[-1] in punctuation_chars:
				# print "MATCH: '%s' is a key with value '%s'" % (word, dictionary[word[:-1]])
				word2 = dictionary[word[:-1]] + word[-1]
				Pirate_words.append(word2)
			# if it doesn't match because of a pluralized word
			# elif word[-1] == 's':
			# 	word2 = dictionary[word[:-1]] + 's'

		# if it doesn't match because of capitalization AND punctuation
		elif dictionary.get(word[:-1].lower()):
			new_word = dictionary.get(word[:-1].lower()) + word[-1]
			Pirate_words.append(new_word.title())


		# if it makes it this far, it is not a match, so toss it back!
		# THIS FOR LOOP HAS NOTHING TO GIVE YOU
		else:
			Pirate_words.append(word)

	Pirate_sentence = " ".join(Pirate_words)
	return Pirate_sentence

def main():
	english_pirate_dict = build_dictionary(file)
	sentence = raw_input("Ahoy! What d\'ya need translated?\n> ")
	# sentence = "Hello, I'm looking for the restroom, and I have a meeting with my lawyer at this restaurant for vegan astronauts. Excuse my bluntness, but New York's hottest club is MADAM. Students, however, prefer JELLY BONES. That place has everything: professors, mescaline, a hotel, screaming bears in chapbook cardigans. You hear me, boy?"

	while sentence != 'q':
		translation = translate(sentence, english_pirate_dict)
		print "...\nOkay, so you want to translate this English sentence:\n\n%s\n\nIf you were speaking Pirate, you would say:\n\n%s" % (sentence, translation)
		sentence = raw_input("Alrighty! What else ya got? If yer done, press 'q' to quit.\n> ")

if __name__ == "__main__":
		main()