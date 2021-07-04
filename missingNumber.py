"""
Given an array of n elements, containing elements belonging to [1, n + 1], 
knowing that the array is missing only one element to have all elements 1 through n + 1, 
find the missing element.

Requirement: O(1) space


Example:

arr = [1,2,4]. the output should be missingNumber(arr) = 3. 
"""
def missingNumber(arr):
    for i in range(1, len(arr) + 2):
        if i not in arr:
            return i