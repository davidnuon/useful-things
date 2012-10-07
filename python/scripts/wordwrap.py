test = """been classified as American Romanticism. It was first published by Richard Bentley in London on October 18, 1851, in an expurgated three-volume edition titled The Whale, and weeks later as a single volume, by New York City publisher Harper and Brothers as Moby-Dick; or, The Whale on November 14, 1851. The book initially received mixed reviews, but Moby-Dick is now considered part of the Western canon,[3] and at the center of the canon of American novels.
"""

other_test = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris posuere augue nec purus pulvinar sagittis sed sit amet augue. Sed lacinia augue ut nisi aliquet nec accumsan arcu aliquet. Donec semper est quis lorem pharetra pellentesque. Nullam sodales leo nec enim aliquet commodo. Proin porttitor, arcu sit amet placerat rutrum, libero nisl porttitor libero, sit amet malesuada eros nulla eu elit. Donec sed elit in odio pellentesque consectetur ac quis libero. Sed tristique lectus a velit consectetur porttitor. Morbi mauris risus, gravida a facilisis ac, elementum non turpis.

Phasellus lacinia nisl enim. Ut vitae nibh quam. Duis malesuada vestibulum tortor ac laoreet. Ut adipiscing tortor sed ligula luctus ultricies gravida sapien eleifend. Ut dictum pretium facilisis. Donec convallis malesuada justo vitae venenatis. Morbi ante sem, mattis posuere consequat id, molestie sed tellus. Mauris ornare rhoncus malesuada.

Morbi condimentum egestas bibendum. Etiam risus urna, tincidunt et malesuada sed, tincidunt quis diam. Phasellus interdum ultrices sem, scelerisque tincidunt leo rutrum ut. Phasellus in turpis leo. Morbi eros dui, ornare sit amet pulvinar eu, dignissim tincidunt lacus. Donec ut velit quam. Fusce nec justo nec massa tincidunt gravida. Sed vestibulum lacus ut purus condimentum id laoreet enim viverra. Etiam magna metus, ultricies nec auctor ut, scelerisque sit amet felis. Aliquam ac quam risus.

Donec lectus erat, feugiat non tristique in, lobortis at mauris. Proin bibendum aliquam elit. Vestibulum nec massa justo, quis dignissim nunc. Duis faucibus malesuada pulvinar. In leo arcu, condimentum sit amet dapibus id, tincidunt in lectus. Nunc sodales nulla pharetra nunc iaculis quis facilisis nisi blandit. Sed sollicitudin, ligula sit amet blandit vulputate, sapien neque convallis lorem, nec lacinia augue nunc porta lorem. Cras tortor sem, varius non ornare vitae, malesuada vel odio. Curabitur nulla tellus, eleifend eu feugiat ut, elementum nec metus. Mauris vehicula nisi vitae lectus condimentum vitae ultrices enim fringilla. Proin imperdiet tristique nunc, a dictum mi viverra at.

Praesent sodales lorem in felis dignissim porttitor. Duis blandit leo eu nisl ullamcorper in fermentum mauris bibendum. Duis lobortis felis et purus aliquam semper eget ut orci. Maecenas interdum congue felis sed viverra. Cras fermentum, nisi in gravida suscipit, nunc est hendrerit leo, sed sollicitudin justo odio ut sem. Ut sit amet lorem non est mattis venenatis. Maecenas eu urna vitae urna aliquam sodales eu non elit. Duis ut malesuada libero. Cras dignissim posuere metus et scelerisque. Morbi luctus augue nunc, ut elementum lacus. Donec sed arcu in tortor ornare mollis. Nunc vitae enim metus, eu pulvinar arcu.
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
		newline = ""
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
		if newline != '':
			newlines.append(newline)

	return newlines

story = wordwrap(strip_unicode(test))
for s in story:
	print s