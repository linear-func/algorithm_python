"""
Bạn được cho trước một số tư nhiên n, bạn có quyền tráo đổi các chữ số của số n.

Số k được tạo thành bằng cách tráo các chữ số trong số n để thành số lớn nhất có thể.
Số h được tạo thành bằng cách tráo các chữ số trong số n để thành số nhỏ nhất có thể.
Hãy đưa ra giá trị của k - h.
"""
def min_max(n):
    arr = [a for a in str(n)]
    max1 = "".join(sorted(arr,reverse = True))
    min1 = "".join(sorted(arr))
    return int(max1)-int(min1)

#JS
function minMax(n){
    const string = n.toString();

    const max = string.split("").sort((a,b) => b - a).join("");
    const min = string.split("").sort((a,b) => a - b).join("");
    
    return Number(max) - Number(min);
}  