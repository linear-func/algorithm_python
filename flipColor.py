"""
Cho 1 mảng color chỉ chứa màu đen hoặc trắng. Màu đen-1, màu trắng-0. Trong 1 thao tác lật
 với t[i] ta có thể đổi tất cả các màu từ vị trí t[i] đến cuối mảng( trắng --> đen, 
 đen --> trắng). Sau 1 loạt các thao tác lật liên tiếp được chứa trong t thì color 
 sẽ như thế nào?

Ví dụ:

Với color = [1,0,0,1] và t = [0,1,2,3] thì flipColor(color, t) = [0,0,1,1]. 
Giải thích: [1,0,0,1] --> [0,1,1,0] --> [0,0,0,1] --> [0,0,1,0] --> [0,0,1,1]. 
Với color = [1,1,1,1,1] và t = [4,3,0] thì flipColor(color, t) = [0,0,0,1,0].
Giải thích: [1,1,1,1,1] --> [1,1,1,1,0] --> [1,1,1,0,1] --> [0,0,0,1,0].
"""
def flipColor(color,t):
    for i in range(len(t)) :
        for j in range(int(t[i]),len(color)):
            color[j] = int(color[j]) + 1
    for j in range(len(color)) :
        if color[j] % 2 == 0: 
                color[j] = 0
        else:
            color[j] = 1
    return color

                