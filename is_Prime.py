#A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers
#Implement a function that determines if a given positive integer is a prime or not. 
#true if n is a prime number, false otherwise.

def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

#check
n = int(input("n = "))
print(is_prime(n))