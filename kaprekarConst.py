"""
Given a 4-digit integer n. Perform these operations:

Change the position of the digits of n to get the largest and smallest numbers.
Calculate the difference between the largest and the smallest numbers.
Repeat the above steps and stop when the difference is 6174.
Count the number of repetitions

6174 is known as Kaprekar's constant

If the difference at a step is equal to 0, return 0 

Example:

For n = 6174 the output should be kaprekarConst(n) = 1
We perform the following operations:
Find the largest and smallest numbers by changing the position of digits: maximum value max = 7614, minimum value min  = 1467
The difference: max- min = 7614 – 1467 = 6174
The result is 6174 so kaperkarConst(n) = 1.
For n = 2222 th output should be kaprekarConst(n) = 0
We perform the following operations:
Find the largest and smallest numbers by changing the position of digits: maximum value max = 2222, minimum value min  = 2222
The difference: max- min = 2222 – 2222= 0
The result is 0 so kaperkarConst(n) = 0. 
"""
def kaprekarConst(n,count=1):
    minn=int("".join(sorted(str(n))))
    maxx=int(str(minn)[::-1]+'0'*(4-len(str(minn))))
    res=maxx-minn
    if res==6174:return count
    elif res==0:return 0
    return kaprekarConst(res,count+1)