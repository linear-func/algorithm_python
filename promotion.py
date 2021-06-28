"""
Giới hạn ký tự: 3000 
Tiếng Việt
Thầy Ba muốn có s cây bút để tặng cho học sinh của mình.

Ở cửa hàng bán bút CODELEARN đang có khuyến mãi như sau: Khi mua x cây bút sẽ được tặng y cây bút nữa.

Hãy đưa ra số bút tối thiểu mà Thầy Ba phải mua để thầy có đủ s cây bút.

Ví dụ:

Với x = 2, y = 1, s = 6, thì promotion(x,y,s) = 4.
Giải thích: Thầy Ba sẽ mua 4 cây bút như sau:
Mua 2 cây bút được khuyến mãi 1 cây -> tổng cộng thầy có 3 cây bút.
Mua thêm 2 cây bút được khuyến mãi 1 cây -> tổng cộng thầy có 6 cây bút.
"""
def promotion(x,y,s):
 return x*(s//(x+y))+min(s%(x+y),x)