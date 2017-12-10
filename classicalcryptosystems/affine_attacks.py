def ciphertext_only(ciphertext, num_alphabets):
    """
    This is a brute force attack. We check every possible alpha, beta pair and
    use it to decrypt our ciphertext.
    The attack returns a dictionary of plaintexts that have been decrypted and
    their associated alpha and beta values.

    Next steps:
     - Run the dictionary values through a function that checks whether a word
       is in the English dictionary to eliminate decryptions that are not
       meaningful.
     - For longer texts, run the decrypted text through a frequency analysis to
       check for possible correct decryptions.

    >>> plaintexts = ciphertext_only('cvvwpm', 26)
    >>> plaintexts[(9, 2)]
    'affine'

    :param ciphertext: The ciphertext that needs to be cracked
    :param num_alphabets: Length of the alphabet that was used
    :return:
    """
    from basicnumbertheory.cryptomath import gcd
    from affine import decode
    plaintexts = {}

    for alpha in range(num_alphabets):
        for beta in range(num_alphabets):
            if gcd(alpha, num_alphabets) == 1:
                plaintexts[(alpha, beta)] = decode(ciphertext, alpha, beta,
                                                   num_alphabets)
    return plaintexts


def known_plaintext(plaintext, ciphertext, num_alphabets):
    """
    Takes in plaintext and corresponding ciphertext. The length of both these
    strings are assumed to be equal

    This method works only if we have at least two letters of the plaintext and
    corresponding letters of the ciphertext.
    Otherwise, it devolves into a brute force method and returns a list of
    possible keys.

    >>> known_plaintext("g", "t", 26)
    [(1, 13), (3, 1), (5, 15), (7, 3), (9, 17), (11, 5), (15, 7), (17, -5), (19, 9), (21, -3), (23, 11), (25, -1)]

    >>> known_plaintext("go", "th", 26)
    return one of these: [(5, 15), (18, 15)]

    >>> known_plaintext("an", "ft", 26)
    None

    >>> known_plaintext("if", "pq", 26)
    (17, 9)

    :param plaintext:
    :param ciphertext:
    :return:
    """

    import numpy as np
    from basicnumbertheory.inv_matrix_mod import inv_matrix_mod
    from basicnumbertheory.cryptomath import gcd

    # If we get one letter of the plaintext we can get a relation between alpha
    # and beta and narrow down the possible keys used
    if len(plaintext) == 1:
        k = []
        for alpha in range(num_alphabets):
            # Checking for all valid alphas and calculating corresponding betas
            if gcd(alpha, num_alphabets) == 1:
                beta = ord(ciphertext) - ord('a') - \
                       (ord(plaintext) - ord('a')) * alpha % num_alphabets
                k.append((alpha, beta))
        return k

    # Setting up the two linear equations as matrices
    m = [[ord(plaintext[0]) - ord('a'), 1],
         [ord(plaintext[1]) - ord('a'), 1]]
    c = [ord(ciphertext[0]) - ord('a'), ord(ciphertext[1]) - ord('a')]

    m_inv = inv_matrix_mod(m, num_alphabets)

    # When the determinant of the matrix and the number of alphabets is not
    # relatively prime,
    if len(m_inv) == 0:
        alpha = []
        for a in range(num_alphabets):
            if (m[0][0] - m[1][0]) * a % 26 == abs(c[0] - c[1]):
                # gcd(alpha, num_alphabets)
                alpha.append(a)
        beta = ord(ciphertext[0]) - ord('a') - (ord(plaintext[0]) - ord('a')) * alpha[0] % 26
        k = [(alpha[0], beta), (alpha[1], beta)]
        return k

    print tuple((np.dot(m_inv, c) % 26).tolist())
