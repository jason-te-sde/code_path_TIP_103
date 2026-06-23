"""
As a time traveler, you've collected a mountain of souvenirs over the course of your travels. You're running out of room to store them all and need to declutter. Given a list of strings souvenirs and a integer threshold, declutter your souvenirs by writing a function declutter() return a list of souvenirs whose frequencies are below the threshold.

def declutter(souvenirs, threshold):
    pass
Example Usage:

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2
Example Output:

["alien egg", "map", "map", "statue"]
["sword"]
"""
# from collections import Counter
# def declutter(souvenirs, threshold):
#     freqs = Counter(souvenirs)
#     return [s for s in souvenirs if freqs[s] < threshold]

# from collections import defaultdict
# def declutter(souvenirs, threshold):
#     freqs = defaultdict(int)
#     for s in souvenirs:
#         freqs[s] += 1
#     return [s for s in souvenirs if freqs[s] < threshold]

def declutter(souvenirs, threshold):
    freqs = {}
    for s in souvenirs:
        freqs[s] = freqs.get(s, 0) + 1
    return [s for s in souvenirs if freqs[s] < threshold]

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2
print(declutter(souvenirs2, threshold))
