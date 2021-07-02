"""
Yasuo Đơn giản 100 Điểm
Giới hạn ký tự: 3000 
English
Given an array of numbers, you should print GCD (greatest common divisor) of all of them.

Example

For a = [1, 2, 3], the output should be gCDofNumbers(a) = 1
For a = [2, 4, 6], the output should be gCDofNumbers(a) = 2
"""
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def gcdOfNumbers(a):
    temp = gcd(a[0],a[1])
    k = len(a)
    for i in range(2,k):
        temp = gcd(temp,a[i])
    return temp