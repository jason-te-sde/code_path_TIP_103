"""
Captain Dread is keeping track of the crew's activities using a log. The logs are represented by a 2D integer array logs where each logs[i] = [pirateID, time] indicates that the pirate with pirateID performed an action at the minute time.

Multiple pirates can perform actions simultaneously, and a single pirate can perform multiple actions in the same minute.

The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes in which the pirate performed an action. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of pirates whose PAM equals j.

Return the array answer as described above.

def counting_pirates_action_minutes(logs, k):
    pass
Example Usage:

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
Example Output:

[0, 2, 0, 0, 0]
[1, 1, 0, 0]

"""
from collections import defaultdict
def counting_pirates_action_minutes(logs, k):
    # time complexity : O(n)
    # space complexity : O(n)
    
    # init
    pam = defaultdict(set)
    for pirate_id, time in logs:
        # add unique minutes in each id, len(pam[pirate_id]) is PAM
        pam[pirate_id].add(time)
    
    res = [0] * k
    
    for actions in pam.values():
        # each pirate's pam
        minutes = len(actions)
        # in case out of range
        if minutes <= k:
            # meet the condition
            res[minutes - 1] += 1
    
    return res
            
        
    


logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
