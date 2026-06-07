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
	res = ""
	n = len(word)
	i = 0
	one_char = ["t", "i"]
	two_char = ["gg", "er"]
	while i < n:
		if i < n - 1 and word[i:i+2].lower() in two_char:
			i += 2
		elif word[i].lower() in one_char:
			i += 1
		else:
			res += word[i]
			i += 1
	print(res)
	return res

        

if __name__ == "__main__":
	word = "Trigger"
	tiggerfy(word)
	word = "eggplant"
	tiggerfy(word)
	word = "Choir"
	tiggerfy(word)