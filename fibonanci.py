import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
 
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

print(isFibonacci(13)) 
#print(isFibonacci(8)) True