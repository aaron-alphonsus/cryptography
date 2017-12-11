def sundaram(n):
    """
    Crosses out all numbers of the form i + j + 2ij for 1 <= i <= j and
    i + j + 2ij <= n to give all primes below n.
    Reference:
        http://www.geeksforgeeks.org/sieve-sundaram-print-primes-smaller-n/

    >>> sundaram(71)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

    >>> sundaram(72)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    >>> sundaram(1000) # doctest: +NORMALIZE_WHITESPACE
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
    613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
    919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    :param n: Upper bound for primes n
    :return: List of primes below n
    """

    # We only need to look at half
    limit = (n-2) / 2
    primes = []

    # Mark all the list positions with a 0 to begin with
    marked = [0]*(limit+1)

    # Mark all numbers of the form i + j + 2ij as 1 where 1 <= i <= j
    for i in range(1, limit+1):
        j = i
        while (i + j + 2*i*j) <= limit:
            marked[i + j + 2*i*j] = 1
            j += 1

    # Add 2 to the list of primes
    if (n > 2):
        primes.append(2)

    # Add all the rest of the primes. 2*i + 1 is a prime (where marked[i] is 0)
    for i in range(1, limit+1):
        if marked[i] == 0:
            primes.append(2*i + 1)

    return primes
