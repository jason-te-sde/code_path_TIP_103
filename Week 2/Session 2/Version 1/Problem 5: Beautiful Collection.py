"""
Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a string collection where each artist in your gallery is represented by a character. The beauty of a collection is defined as the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its substrings (subcollections), not just of the collection itself.

def beauty_sum(collection):
    pass
Example Usage:

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))
Example Output:

5
Example 1 Explanation: The substrings with non-zero beauty are 
["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

17
"""
def beauty_sum(collection):
    n = len(collection)
    res = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            c = collection[j]
            freq[c] = freq.get(c, 0) + 1
            res += max(freq.values()) - min(freq.values())
    return res

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))