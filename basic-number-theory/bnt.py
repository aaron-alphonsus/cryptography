# All these algorithms expect positive numbers. Providing negative numbers
# doesn't seem useful right now for my application. If it turns out to be,
# negative functionality will be added


def gcd(a, b):
    """
    Source: Introduction to Algorithms - Cormen, Leiserson, Rivest, Stein

    >>> gcd(69, 3)
    3
    >>> gcd(-69, -3)
    3
    >>> gcd(3, 69)
    3
    >>> gcd(5, 7)
    1

    :param a: first number
    :param b: second number
    :return: greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def extendedgcd(a, b):
    """
    Reference: http://anh.cs.luc.edu/331/notes/xgcd.pdf
    TODO: Mention this reference in the .md

    >>> extendedgcd(26, 9)
    (1, -1, 3)
    >>> extendedgcd(9, 26)
    (1, 3, -1)
    >>> extendedgcd(26, 6)
    (2, 1, -4)

    :param a: first number
    :param b: second number
    :return: List containing gcd, x, and y: (gcd(a,b), x, y)
    """
    # You could store values at each step of the algorithm and then 'walk back'
    # to calculate x, y and the gcd. Or, you could examine the recurrence
    # relation and see that at each step, all you need to calculate the 'new'
    # x and y is the previous x and y. The value you have at the end of the
    # iteration is the required equation with x, y and gcd
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a / b
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        a, b = b, a % b
        # print "q =", q
        # print "x, prevx =", x, prevx
        # print "y, prevy =", y, prevy
        # print "a, b= ", a, b
    return a, prevx, prevy


def findModInverse(a, b):
    """
    Does the extended gcd algorithm and checks the gcd. If the gcd is 1, the
    smallest positive modular inverse is returned. If gcd is not 1, the
    modular inverse doesn't exist and -1 is returned (valid since we return the
    smallest positive modular inverse otherwise)

    Testing the normal case
    >>> findModInverse(9, 26)
    3
    >>> findModInverse(26, 9)
    8
    >>> findModInverse(17, 3120)
    2753
    >>> findModInverse(6, 26)
    -1

    :param a: first number
    :param b: second number
    :return: Smallest positive mod inverse of a and b. -1 if it doesn't exist
    """
    if extendedgcd(a, b)[0] != 1:
        # We always return the smallest positive mod inverse so this is good.
        return -1
    else:
        if extendedgcd(a, b)[1] < 0:
            return extendedgcd(a, b)[1] + b
        else:
            return extendedgcd(a, b)[1]
