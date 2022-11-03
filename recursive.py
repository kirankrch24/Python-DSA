# find the n! 

def factorial(n):
    if n == 0 or n == 1:
        return n
    elif n<0:
        return -1
    else:
        result = n * factorial(n-1)
        return result

x = factorial(5)

print(x)