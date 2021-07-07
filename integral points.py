"""
Cho ba số nguyên n,m và k, xét tập hợp S gồm tất cả các điểm (x, y) với hoành độ x thỏa 0 <= x <= n và tung độ y thỏa 0 <= y <= m.

Yêu cầu: Tính số cặp điểm (A, B) với cả A và B đều thuộc tập S sao cho F(A, B) = k.

Lưu ý: cặp (A, B) và (B, A) chỉ được tính 1 lần
"""
def integral_points(n,m,k):
    lis = []
    for i in range(n+1):
        for j in range(m+1):
            arr = [i,j]
            lis.append(arr)
    f = len(lis)
    count = 0
    for i in range(f):
        for j in range(i,f):
            a = lis[i][0] - lis[j][0]
            b = lis[i][1] - lis[j][1]
            if math.gcd(a,b)+1 == k:
                count += 1
    return count
