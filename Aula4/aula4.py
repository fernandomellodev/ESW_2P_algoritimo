"""fibonacci"""
"""fibonacci(3) = fibonacci(2) + fibonacci (i)
fibonacci (4) = fibonacci(3) + fibonacci (2)
fibonacci (n) = fibonacci(n -1) + fibonacci(n-2)

"""


def fibonacci (n):

    if n == 0 or n ==1:
        return n
    return  fibonacci(n -1) + fibonacci(n-2)

resultado = fibonacci(5)
print (resultado)
