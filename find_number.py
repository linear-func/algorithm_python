""" tìm chuỗi số có N chữ số trong một số n bất kì được nhập vào, sao cho
chữ số lớn nhất trừ chữ số nhỏ nhất trong N là nhỏ nhất và N là số nhỏ nhất
trong những số tìm được. 
"""
def find(n):
    str1 = str(n)
    lis = []
    lis1 = []
    lis2 = []
    for i in range(len(str1)):
        lis.append(str1[i])
    for i in range(len(str1)- N + 1):
        T = int(max(lis[i:i+N])) - int(min(lis[i:i+N]))
        lis1.append(T)
    mini = min(lis1)
    for i in range(len(str1)- N + 1):
        if int(max(lis[i:i+N])) - int(min(lis[i:i+N])) == mini:
            lis2.append("".join(lis[i:i+N]))
    print(lis2)
    return min(lis2)

n = 1975797531
N = 2
print(find(n))
