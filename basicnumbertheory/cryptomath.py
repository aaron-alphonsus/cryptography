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
    >>> gcd(165, 561)
    33

    :param a: first number
    :param b: second number
    :return: greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(abs(b), abs(a % b))


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


def is_prime(n, r):
    """

    >>> is_prime(561, 1)
    0
    >>> is_prime(56, 1)
    0
    >>> is_prime(2, 1)
    2

    :param n: Number to be tested
    :param r: Number of times to run the algorithm
    :return: 2 if definite prime, 1 if probable prime, 0 if definite composite
    """
    # TODO: Add in more rounds

    import random

    # Let n > 1 be an odd integer (eliminate even numbers)
    if n == 2:
        return 2
    if n & 1 == 0:
        return 0

    # Write n-1 = (2^k)*m with m odd.
    m = n-1
    k = 0
    while m & 1 == 0:
        m /= 2
        k += 1
    # print "(2^" + str(k) + ")*" + str(m)

    # Choose a random integer a with 1 < a < n - 1
    a = random.randint(2, n-2)                             # end-points included
    # print "a =", a

    # Compute b(0) = a^m (mod n)
    b = pow(a, m, n)
    # print "b =", b
    # If b(0) = (+-) 1 (mod n) stop and declare n probable prime
    if b == 1 or b == -1:
        return 1

    for i in range(k - 2):
        b = pow(b, 2, n)
        # print "b(" + str(i+1) + ") = " + str(b)
        if b == 1:
            return 0
        elif b == -1:
            return 1
    b = pow(b, 2, n)
    # print "last b = " + str(b)
    if not b == -1:
        return 0

    return 1                                  # TODO: verify if this should be 2


def random_prime(b):
    # WARNING: Not cryptographically secure
    pass
