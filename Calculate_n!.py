# find the n! 

# we used recursive method to find n!

# we defined n function to calculate n!
def factorial(n):
    # 0 and 1 factorial is 0 and 1 itself
    if n == 0 or n == 1:
        return n
    # factorial of negative number doesn't exists
    elif n<0:
        return -1
    # n factorial is n*(n-1)!, we calling factorial function but with different value this time i.e(n-1
    else:
        result = n * factorial(n-1)
        return result

x = factorial(5)

print(x)
