import sys

def strip_unicode(string):
	out = ""
	for n in string:
		out += [n, '-'][ord(n) > 127]
	return out

def count_char(string, char='\t'):
	count = 0
	for n in string:
		if n == char:
			count += 1
	return count

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
				current_length = 0
				if '\t' in newline:
					current_length = (count_char(newline)*3)	
				current_length += len(word)
				newline = '\t'*(count_char(newlines[-1])+1) + '  ' + word + ' '
		if newline != '':
			newlines.append(newline)

	return "\n".join(newlines)

print wordwrap(strip_unicode(sys.stdin.read()))
