
def factorial(n):
    if n < 0:
        return "Sorry, wrong number"
    elif n <= 1:
        result = n
        return result
    elif n > 1:
        return factorial(n-1)*n
