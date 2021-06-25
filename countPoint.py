"""
Cho một số nguyên n. Hãy tìm tổng số chấm trên các hình ngũ giác tính từ 2 đến n (lồng nhau).

Ví dụ:

Với n = 2. Đầu ra countPoints(n) = 5. 

Với n = 3. Đầu ra countPoints(n) = 12.     

Đầu vào/Đầu ra:

[Thời gian chạy] 0.5s với C++, 3s với Java và C#, 4s với Python, Go và JavaScript.
[Đầu vào] integer n.
      0<= n <=10^5

[Đầu ra] long long
Kết quả yêu cầu đề bài.

"""
def countPoints2(n):
    x = 1 
    if n == 0 :
        return 0 
    elif n == 1 :
        return 1
    else:
        for i in range(2,n+1):
            x += (i*3-2) 
        return int(x)
n = int(input("n= "))
print(countPoints2(n))