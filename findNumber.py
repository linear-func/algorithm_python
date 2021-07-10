"""
Một số được gọi là số tăng giảm nếu các chữ số trong số này tạo thành một dãy số giảm dần (số đứng sau luôn nhỏ hơn hoặc bằng số đứng trước) hoặc dãy số tăng dần (số đứng sau luôn lớn hơn hoặc bằng số đứng trước). Ví dụ:

Các số tăng giảm: 7, 22, 6522, 4667, 9651, 7899, ...
Các số không phải là số tăng giảm: 121, 486, 9878, ...
Cho trước số nguyên n, bạn hãy viết hàm trả về số tăng giảm nhỏ nhất mà lớn hơn hoặc bằng n.

Ví dụ:

Với n = 8 thì output là findNumber(n) = 8.
Với n = 565 thì output là findNumber(n) = 566.
"""
def findNumber(n):
    run1 = 0
    while run1 == 0:
        giam = 0
        tang = 0
        s = str(n)
        for i in range(len(s)-1):
            if int(s[i]) >= int(s[i+1]):
                giam += 1 #"Ham giam"
            if int(s[i]) <= int(s[i + 1]):
                tang += 1 #"Ham tang"
        if giam == len(s) - 1:
            answer = int(s)
            run1 = 1
        elif tang == len(s) - 1:
            answer = int(s)
            run1 = 1
        else:
            n = int(s)
            n += 1
    return answer