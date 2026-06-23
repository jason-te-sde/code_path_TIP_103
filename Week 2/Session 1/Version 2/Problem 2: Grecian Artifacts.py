"""
You've spent your last few trips exploring different periods of Ancient Greece. During your travels, you discover several interesting artifacts. Some artifacts appear in multiple time periods, while others in just one.

You are given two lists of strings artifacts1 and artifacts2 representing the artifacts found in two different time periods. Write a function find_common_artifacts() that returns a list of artifacts common to both time periods.

def find_common_artifacts(artifacts1, artifacts2):
    pass
Example Usage:

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))
Example Output:

 ["Golden Vase", "Bronze Shield"]
"""

# # Unordered
# def find_common_artifacts(artifacts1, artifacts2):
#     return list(set(artifacts1) & set(artifacts2))

# Ordered
def find_common_artifacts(artifacts1, artifacts2):
    set2 = set(artifacts2)
    return [a for a in artifacts1 if a in set2]

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))