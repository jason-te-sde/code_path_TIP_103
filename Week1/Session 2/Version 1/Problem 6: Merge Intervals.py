"""
You are given an array of intervals, where each interval is represented as [start, end].

Write a function merge_intervals(intervals) that merges all overlapping intervals and returns a new array of the merged, non-overlapping intervals.

def merge_intervals(intervals):
	pass
Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
Example Output:

[[1, 6], [8, 10], [15, 18]]
[[1, 5]]
"""
def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]
    
    for cur in sorted_intervals[1:]:
        last = merged[-1]
        if last[1] >= cur[0]:
            last[1] = max(last[1], cur[1])
        else:
            merged.append(cur)
    
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))
            
 