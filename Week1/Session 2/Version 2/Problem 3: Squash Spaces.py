"""
Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.

def squash_spaces(s):
    pass
Example Usage

s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)
Example Output:

"Up, up, and away!"
"With great power comes great responsibility."
"""
# def squash_spaces(s):
#     stripped = s.strip()
#     splitted = stripped.split()
    
#     return " ".join(splitted)

def squash_spaces(s):
    i = 0
    res = []
    while i < len(s):
        while i < len(s) and s[i] == " ":
            i += 1
        while i < len(s) and s[i] != " ":
            res.append(s[i])
            i += 1
        res.append(" ")
    
    return "".join(res[:-1])

s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))
    