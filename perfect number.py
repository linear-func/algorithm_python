#perfect number
#find all perfect numbers in the interval [a,b]
#the number n is perfect when the sum of the positive divisors of n is 2n
def fine_UC(n):
	temp = []
	for i in range(1,n):
		if n % i == 0:
			temp.append(i)
	return sum(temp)

def perfectNumber(a,b):
	temp2 = []
	for i in range(a,b+1):
		if fine_UC(i) == i:
			temp2.append(i)
	print(temp2)
	return len(temp2)

a = int(input("a = "))
b = int(input("b = "))
if 1<=a<=b<=10000:
	print("have", perfectNumber(a,b), "perfect number ") 
else: 
	print("none")


