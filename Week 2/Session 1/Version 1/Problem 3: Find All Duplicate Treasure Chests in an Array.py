"""
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):
    pass
Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
Example Output:

[2, 3]
[1]
[]
"""
# from collections import Counter
# def find_duplicate_chests(chests):
#     counts = Counter(chests)
#     res = []
#     for key, value in counts.items():
#         if value == 2:
#             res.append(key)
#     res.sort()
#     return res
def find_duplicate_chests(chests):
    freq = {}
    for chest in chests:
        freq[chest] = freq.get(chest, 0) + 1
    return [val for val, count in freq.items() if count > 1]

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))