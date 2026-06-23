"""
In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls across different rooms. You are given a dictionary library_catalog that maps room names to the number of scrolls that room should have and a second dictionary actual_distribution that maps room names to the number of scrolls found in that room after the temporal rift.

Write a function analyze_library() that determines if any room has more or fewer scrolls than it should. The function should return a dictionary where the keys are the room names and the values are the differences in the number of scrolls (actual number of scrolls - expected number of scrolls). You must loop over the dictionaries to compute the differences.

def analyze_library(library_catalog, actual_distribution):
    pass
Example Usage:

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))
Example Output:

{'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}
"""

def analyze_library(library_catalog, actual_distribution):
    res = {}
    
    for room, number in actual_distribution.items():
        original_number = library_catalog[room]
        res[room] = number - original_number
    
    return res

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))