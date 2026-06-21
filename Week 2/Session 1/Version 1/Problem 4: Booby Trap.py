"""
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function can_make_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

def can_make_balanced(code):
    pass
Example Usage:

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
"""
from collections import Counter
def can_make_balanced(code):
    freq = Counter(code)
    
    for ch in freq:
        freq[ch] -= 1
        
        remaining = [c for c in freq.values() if c > 0]
        
        if len(set(remaining)) <= 1:
            return True
        
        freq[ch] += 1
    
    return False
    
    

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
