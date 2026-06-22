"""
Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

Return a list of groups such that each pirate i is in a group of size group_sizes[i].

Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

def organize_pirate_crew(group_sizes):
    pass
Example Usage:

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
Example Output:

[[5], [0, 1, 2], [3, 4, 6]]
[[1], [0, 5], [2, 3, 4]]
"""

# def organize_pirate_crew(group_sizes):
#     groups = {}
#     res = []
#     for i, size in enumerate(group_sizes):
#         # init
#         if size not in groups:
#             groups[size] = []
#         # add people
#         groups[size].append(i)
#         # check the size
#         if len(groups[size]) == size:
#             res.append(groups[size])
#             # pop it
#             groups[size] = []
#     # res.sort(key=lambda x: len(x))
    
#     # time complexity : O(n)
#     # space complexity: O(n)
            
#     return res

from collections import defaultdict
def organize_pirate_crew(group_sizes):
    groups = defaultdict(list)
    res = []
    
    for i, size in enumerate(group_sizes):
        groups[size].append(i)
        if len(groups[size]) == size:
            res.append(groups[size])
            groups[size] = []
    # res.sort(key=lambda x: len(x))
    
    return res
        


group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 