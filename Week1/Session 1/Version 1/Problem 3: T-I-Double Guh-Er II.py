"""
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass
Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"chor"

"""

def tiggerfy(word):
	res = []
	n = len(word)
	word = word.lower()
	i = 0
	one_char = {"t", "i"}
	two_char = {"gg", "er"}
	while i < n:
		if i < n - 1 and word[i:i+2] in two_char:
			i += 2
		elif word[i] in one_char:
			i += 1
		else:
			res.append(word[i])
			i += 1
	return "".join(res)

        

if __name__ == "__main__":
	word = "Trigger"
	print(tiggerfy(word))

	word = "eggplant"
	print(tiggerfy(word))

	word = "Choir"
	print(tiggerfy(word))
	
	# Additional edge cases
	test_cases = [
        ("Trigger", "r"),           # Basic example + case handling
        ("", ""),                   # Empty string
        ("abc", "abc"),             # No removable characters
        ("tti", ""),                # All removable characters
    ]
    
	for word, expected in test_cases:
		result = tiggerfy(word)
		status = "✓" if result == expected else "✗"
		print(f"{status} tiggerfy('{word}') = '{result}' (expected '{expected}')")