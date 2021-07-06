"""
Cho mảng arr gồm các số nguyên. Hãy chia mảng này thành 2 mảng con liên tiếp sao cho tổng của tích các phần tử
 trong 2 mảng này là lớn nhất. Do kết quả có thể rất lớn nên sẽ được chia lấy dư cho 10^9 + 7.

Ví dụ:

Với arr = [2,4,1,3] thì maxProduct(arr) = 14.
Giải thích: ta có thể chia thành hai mảng con [2] và [4,1,3]. 
Với arr = [-1,3,4,-2] thì maxProduct(arr) = -11.
Giải thích: ta có thể chia thành hai mảng con [-1,3] và [4,-2]. 
"""
def maxProduct(arr):
    lis = []
    tich1=tich2=1
    k=len(arr)
    for i in range(1,k):
        for a in range(0,i):
            tich1 *= arr[a]
        for b in range(i,k):
            tich2 *= arr[b]
        lis.append(tich1+tich2)
        tich1=tich2=1
    return max(lis)