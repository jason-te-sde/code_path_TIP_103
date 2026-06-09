"""
Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that represents the start and end of another interval.

Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

You don't need to modify intervals in-place. You can make a new array and return it.

def insert_interval(intervals, new_interval):
    pass
Example Usage

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)
Example Output:

[[1, 5], [6, 9]]
[[1, 2], [3, 10], [12, 16]]
"""
def insert_interval(intervals, new_interval):
    res = []
    i = 0
    n = len(intervals)
    
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    
    res.append(new_interval)
    
    while i < n:
        res.append(intervals[i])
        i += 1

    return res

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert_interval(intervals, new_interval))
