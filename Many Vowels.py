"Create a function that takes a string and returns the number (count) of vowels contained within it."
	return len([c for c in txt if c.lower() in 'aeiou'])
