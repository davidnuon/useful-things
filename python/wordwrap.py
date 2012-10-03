test = """been classified as American Romanticism. It was first published by Richard Bentley in London on October 18, 1851, in an expurgated three-volume edition titled The Whale, and weeks later as a single volume, by New York City publisher Harper and Brothers as Moby-Dick; or, The Whale on November 14, 1851. The book initially received mixed reviews, but Moby-Dick is now considered part of the Western canon,[3] and at the center of the canon of American novels.
"""

def strip_unicode(string):
	out = ""
	for n in string:
		out += [n, '-'][ord(n) > 127]
	return out

def wordwrap(string, MAXLEN = 80):
	lines = string.split('\n')
	newlines = []
	newline = ""
	for line in lines:
		words = line.split(' ')
		current_length = 0
		
		for word in words:
			if len(word) + current_length < MAXLEN:
				newline +=  word
				newline += " "
				current_length += len(word) + 1 # We add one for space
			else:
				newlines.append(newline)
				current_length = len(word)
				newline = word

		newlines.append('')

	return newlines

story = wordwrap(strip_unicode(test))
for s in story:
	print s