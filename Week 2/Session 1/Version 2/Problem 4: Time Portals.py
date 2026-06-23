"""
In your time travel adventures, you are given an array of digit strings portals and a digit string destination. Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

def num_of_time_portals(portals, destination):
    pass
Example Usage:

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
Example Output:

4
2
6
"""

# def num_of_time_portals(portals, destination):
#     remanings = {}
#     res = 0
#     for p in portals:
#         for r in remanings.keys():
#             if r + p == destination:
#                 res += remanings[r]
#             if p + r == destination:
#                 res += remanings[r]
                
#         remanings[p] = remanings.get(p, 0) + 1

#     return res

# from collections import Counter
# def num_of_time_portals(portals, destination):
#     freqs = Counter(portals)
#     res = 0
    
#     for p in portals:
#         if destination[:len(p)] == p:
#             r = destination[len(p):]
#             res += freqs[r]
#             if r == p:
#                 res -= 1
#     return res       

def num_of_time_portals(portals, destination):
    remainings = {}
    res = 0
    for p in portals:
        left = destination[:len(p)]
        right = destination[-len(p):]
        if left == p:
            res += remainings.get(destination[len(p):], 0)
        if right == p:
            res += remainings.get(destination[:-len(p)], 0)
        
        remainings[p] = remainings.get(p, 0) + 1
    
    return res

# from collections import defaultdict
# def num_of_time_portals(portals, destination):
#     remainings = defaultdict(int)
#     res = 0
    
#     for p in portals:
#         left = destination[:len(p)]
#         right = destination[-len(p):]
#         if left == p:
#             res += remainings[destination[len(p):]]
#         if right == p:
#             res += remainings[destination[:-len(p)]]
        
#         remainings[p] += 1
    
#     return res

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))