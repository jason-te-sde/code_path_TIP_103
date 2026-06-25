"""
As a time traveling linguist, you are analyzing texts written in an ancient script. However, some words in the text are illegible and can't be deciphered. Write a function find_most_frequent_word() that accepts a string text and a list of illegible words illegibles and returns the most frequent word in text that is not an illegible word.

def find_most_frequent_word(text, illegibles):
    pass
Example Usage:

paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 
Example Output:

a

ball
Example 2 Explanation:
"hit" occurs 3 times, but it is an unknown word.
"ball" occurs twice (and no other word does), so it is the most frequent legible word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is illegible.

"""
"""
1. Understand:
    - read problem
    - restate the problem in own words
        find the most frequent word in text which is not in illegibles.
    - questions? example usage / expected output / edge cases
        removing punctuation, spaces
        make all letter lowercase
2. Plan:
    - general idea
        1. split the string `text` into a list of words
        2. convert `illegibles` to set
        3. build frequency map with words not in `illegibles`
        4. return the most frequent word in frequency map
    - break down the problem into sub problems
    - translate each subproblem into pseudocode
        
3. Implement.
"""

from collections import Counter
import re
def find_most_frequent_word(text, illegibles):
    # 1. split the string `text` into a list of words
    # punctuation = set(".,!?;:'\"()[]{}<>-/\\@#$%^&*_~")
    # clean_text = "".join(c.lower() if c not in punctuation else " " for c in text)
    # words_list = clean_text.split()
    words_list = re.findall(r"[a-z]+", text.lower())
    
    # 2. convert `illegibles` to set
    illegibles_set = {w.lower() for w in illegibles}
    
    # 3. build frequency map with words not in `illegibles`
    freqs = Counter(word for word in words_list if word not in illegibles_set)
    # 4. return the most frequent word in frequency map
    # top_word = max(freqs, key=freqs.get)
    if not freqs:
        return None
    return freqs.most_common(1)[0][0]
    

paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 