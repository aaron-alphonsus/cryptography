def shanks(n, k):
    """
    A method for integer factorization. An improvement on Fermat's factorization
    method.
    Reference:
    https://en.wikipedia.org/wiki/Shanks%27_square_forms_factorization#Algorithm

    >>> shanks(11111, 1)
    (41, 271)
    >>> shanks(21, 4)
    (3, 7)

    :param n: Number to find the factor of
    :param k: Small multiplier
    :return: False if unable to factor, non-trivial factors otherwise
    """
    from basicnumbertheory.cryptomath import is_square, is_prime, gcd
    from math import floor, sqrt

    if is_prime(n) or is_square(n):
        return False

    # 2 main loops:
    #  - Until you find q is a perfect square
    #  - Until p equals previous p

    # Initializations for first loop
    p0 = floor(sqrt(k*n))
    q0 = 1
    q1 = k*n - p0*p0

    p = p0
    q_prev, q = q0, q1

    # Loop until you find q is a perfect square
    while True:
        b = floor((p0 + p)/q)
        p_prev = p
        p = b*q - p

        save = q
        q = q_prev + b*(p_prev - p)
        q_prev = save

        # print p, q_prev, b
        if is_square(q):
            break

    # Initializations for the second loop
    p_prev = p
    b0 = floor((p0 - p_prev) / sqrt(q))
    # print b0, p0, p_prev, q
    p0 = b0*sqrt(q) + p_prev
    p = p0

    q0 = sqrt(q)
    q1 = (k*n - p0**2) / q0
    q_prev, q = q0, q1

    # print p0, q0, b0

    # Loop until p equals the previous p value
    while True:
        p_prev = p
        b = floor((p0 + p_prev) / q)
        p = b*q - p_prev

        # print p, q, b=
        save = q
        q = q_prev + b*(p_prev - p)
        q_prev = save

        if p_prev == p:
            break

    # Take the gcd and check if it's equal to 1 or n. If it isn't you have found
    # non-trivial factor. Else, do the algorithm for another value of k.
    f = gcd(n, p)
    if f != 1 and f != n:
        return int(f), int(n/f)
    else:
        print "Try different k value"
        return False

