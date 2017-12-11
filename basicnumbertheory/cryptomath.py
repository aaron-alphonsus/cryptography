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
    Next Steps: increase number of returned 2s (keep a list of small primes)

    (1/4)^r chance that n is prime.

    >>> is_prime(561, 10)
    0
    >>> is_prime(56, 1)
    0
    >>> is_prime(2, 1)
    2
    >>> is_prime(563, 500)
    1
    >>> is_prime(1, 7)
    0
    >>> is_prime(1, 7)
    0
    >>> is_prime(643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153, 64)
    1
    >>> is_prime(743808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153, 64)
    0

    :param n: Number to be tested
    :param r: Number of times to run the algorithm
    :return: 2 if definite prime, 1 if probable prime, 0 if definite non-prime
    """

    import random

    if n < 2:
        return 0
    # Let n > 1 be an odd integer (eliminate even numbers)
    if n == 2:
        return 2
    if n & 1 == 0:
        return 0

    if n == 3:  # Avoids issue with randint(2, 3-2)
        return 2

    # Write n-1 = (2^k)*m with m odd.
    m = n-1
    k = 0
    while m & 1 == 0:
        m /= 2
        k += 1
    # print "(2^" + str(k) + ")*" + str(m)

    a = []
    ans = []
    for trial in range(r):
        # Choose a random integer a with 1 < a < n - 1
        rand = random.randrange(2, n - 2)                  # end-points included
        a.append(rand)
        # print "a =", a

        # Compute b(0) = a^m (mod n)
        b = pow(a[trial], m, n)
        # print "b =", b
        # If b(0) = (+/-) 1 (mod n) stop and declare n probable prime
        # Note: -1 (mod n) = n-1 (mod n)
        if b == 1 or b == n-1:
            ans.append(1)
        else:
            # Calculate sequence of b^2 (mod n) and check whether probable prime
            for i in range(k - 2):
                b = pow(b, 2, n)
                # print "b(" + str(j+1) + ") = " + str(b)
                if b == 1:
                    ans.append(0)
                    break
                if b == n-1:
                    ans.append(1)
                    break
            else:                           # if for loop doesn't hit the breaks
                b = pow(b, 2, n)
                # print "last b = " + str(b)
                if not b == n-1:
                    ans.append(0)
                else:
                    ans.append(1)
            if ans[trial] == 0:   # We can quit early because definite non-prime
                return 0
    # If you have reached here, you have appended 1 for every r
    # (i.e. probably prime)
    return 1


def random_prime(b):
    """
    Source: https://langui.sh/2009/03/07/generating-very-large-primes/
     - helped out by adding a max (just in case)

    WARNING: Not cryptographically secure

    TODO: Test output value with some prime testing library

    usage: random_prime(1024)

    :param b: See returned value
    :return: Generates random prime between 2^(b+1)-1 and 2^b - 1
    """
    import math
    import random
    confidence = 64

    r_max = 100 * (math.log(b, 2) + 1)                  # max number of attempts
    r = r_max
    while r > 0:
        n = random.randrange(2**b - 1, 2**(b+1) - 1)
        # print n
        r -= 1
        if is_prime(n, confidence):
            print n
            return
    return "Failure after " + str(r_max) + " tries."


def factor(n, m):
    """
    We assume that n is a composite number.

    >>> factor(987, 2)
    (3, 329)
    >>> factor(987, 0)
    (21, 47)

    :param n:
    :param m:
    :return:
    """
    # Fine! If you're going to give me a prime...
    if is_prime(n, 64):
        return n, 1

    if m == 0:
        return fermat_factor(n)
    elif m == 1:
        return pollard_rho_factor(n)
    else:
        return pollard_pminus1_factor(n)


def fermat_factor(n):
    import math
    s = 1
    while not is_square(n + s**2):
        s += 1
    return int(math.sqrt(n + s ** 2)) - s, int(math.sqrt(n + s ** 2)) + s


def is_square(x):
    """
    Brought to you by:
        https://stackoverflow.com/questions/2489435/
        how-could-i-check-if-a-number-is-a-perfect-square
    """
    y = x // 2
    seen = {y}
    while y * y != x:
        y = (y + (x // y)) // 2
        if y in seen:
            return False
        seen.add(y)
    return True


def pollard_pminus1_factor(n):
    """
    Pollard p-1 implementation from the textbook

    >>> pollard_pminus1_factor(562)
    (281, 2)
    >>> pollard_pminus1_factor(561)
    (3, 187)
    >>> pollard_pminus1_factor(987)
    (3, 329)

    :param n: Number to factor
    :return: The factors if it was able to factor, False otherwise
    """
    # choose a > 1 (often a=2)
    a = 2

    # choose bound B
    # Compute b = a^(B!)(mod n) as follows
    #   Let b(1) = a (mod n) and
    #       b(j) = b(j-1)^j (mod n) [from j=2 onwards I'm guessing]
    # Then, b(B) = b (mod n). Let d = gcd(b-1, n)
    #   if 1 < d < n, d is a nontrivial factor of n
    bound = 2
    while 1:                               # Since we only get composite numbers
        b = a % n
        for j in range(2, bound):
            b = pow(b, j, n)
        d = gcd(b-1, n)
        if 1 < d < n:
            return d, n/d
        bound += 1


def pollard_rho_factor(n):
    pass


