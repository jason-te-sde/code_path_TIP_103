"""
Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, you can choose any character of map2 and replace it with another character.

Return the minimum number of steps to make map2 an anagram of map1.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

def min_steps_to_match_maps(map1, map2):
    pass
Example Usage:

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
Example Output:

1
6
0
"""
from collections import Counter
def min_steps_to_match_maps(map1, map2):
    freq1 = Counter(map1)
    freq2 = Counter(map2)
    
    steps = 0
    for c in freq2:
        # same length, only need to calculate the diff
        steps += max(0, freq2[c] - freq1[c])
    
    return steps
        

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))