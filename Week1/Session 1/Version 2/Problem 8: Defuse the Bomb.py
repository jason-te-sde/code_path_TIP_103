"""
Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!

def defuse(code, k):
	pass
Example Usage:

code = [5, 7, 1, 4]
k = 3
defuse(code, k)

code = [1, 2, 3, 4]
k = 0
defuse(code, k)

code = [2, 4, 9, 3]
k = -2
defuse(code, k)
Example Output:

[12, 10, 16, 13]
[0, 0, 0, 0]
[12, 5, 6, 13]
"""
def defuse(code, k):
    n = len(code)
    res = [0] * n
    
    if k == 0:
        return res
    
    if k > 0:
        left = 1
        right = 1 + k
    else:
        left = n - abs(k)
        right = n
    
    window_sum = sum(code[left : right])
    for i in range(n):
        res[i] = window_sum
        window_sum = window_sum - code[(left + i) % n] + code[(right + i) % n]
        
    
    return res

code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))
