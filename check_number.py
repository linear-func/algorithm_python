"""
Một số là số đặc biệt khi mà các chữ số trong nó không bị trùng lặp, ví dụ 123, 3127, 4897 là các số đặc biệt.

Nhập vào một số nguyên dương n, hãy kiểm tra xem n có phải là số đặc biệt hay không. Trả về true nếu phải và ngược lại.

Ví dụ:

Với n = 123 thì checkSpecialNumber(n) = true.

Với n = 112 thì checkSpecialNumber(n) = false.
Đầu vào/Đầu ra:

[Thời gian chạy] 0.5s với C++, 3s với Java và C#, 4s với Python, Go và JavaScript.

[Đầu vào] Long n.
0 ≤ n ≤ 1015.

[Đầu ra] Bool.
Trả về true nếu phải và ngược lại.
"""
def check_special_number(n):
    str1 = str(n)
    k = len(str(n))
    for i in range(k):
        for j in range(i+1,k):
            if str1[i] == str1[j]:
                return False
    return True

#cach 2
def check_special_number(n):
    count=0
    for i in range(1,n):
        if str(n).count(str(i))>1:
            count=count+1
    if count==0:
        return True
    else:
        return False