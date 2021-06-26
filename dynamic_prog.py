n = int(input("nhap so so hang: "))
print("nhap",n,"so hang")
a = []
for i in range(n):
  x = int(input())
  a.append(x)
l = []
for i in range(n):
  l.append(0)
l[0] = a[0]
l[1] = max(a[0],a[1])
for i in range(2,n) :
  x = max(l[i-2],0)
  l[i] = max(l[i-1],a[i] + x)
print("tong gia tri lon nhat", l[n-1])