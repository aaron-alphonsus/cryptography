def ciphertext_only(ciphertext, num_alphabets):
    """
    This is a brute force attack. We check every possible alpha, beta pair and
    use it to decrypt our ciphertext.
    The attack returns a dictionary of plaintexts that have been decrypted and
    their associated alpha and beta values.

    Next steps:
     - Running the dictionary values through a function that checks whether a
       word is in the English dictionary to eliminate decryptions that are not
       meaningful.
     - For longer texts, running the decrypted text through a frequency analysis
       to check for possible correct decryptions.

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
    possible = 0

    for alpha in range(num_alphabets):
        for beta in range(num_alphabets):
            if gcd(alpha, num_alphabets) == 1:
                plaintexts[(alpha, beta)] = decode(ciphertext, alpha, beta,
                                                   num_alphabets)
                # print (alpha, beta), ":", decode(ciphertext, alpha, beta)
                # print (alpha, beta)
    return plaintexts