"""
A sum s looks like this: S = 13 + 33 + 53 + ... + (2n-1) 3.
Given an integer n, write the function that returns the sum of s using the 
same formula as above. If the sum of s is not found, return -1.

For example:

For n = 7 then sum_of_cubes_odd_number (n) = 4753.
For n = 13 then sum_of_cubes_odd_number (n) = 56953.
For n = 27 then sum_of_cubes_odd_number (n) = 1062153.
Input/Output:

[Execution time limit] 0.1s for C++; 0.6s for Java,C#; 0.8s for Python,Go,Js.
Input: interger n
         |n|<=int.Max 

Output: long 
The sum S. if the result is too large, divide the result by 109 + 7. (If the input is invalid, return -1).       
"""
def sum_of_cubes_odd_number(n):
    s = 0
    if n <= 0:
        return -1
    else:
        for i in range(1,n+1):
            s += (2*i-1)**3
    return s %( 10**9 + 7)
