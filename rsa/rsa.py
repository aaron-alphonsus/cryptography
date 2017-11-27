# TODO: Review where public and private variables should be placed
# TODO: Documentation
# TODO: Try larger primes - check time


def decrypt(ciphertext):
    """
    Example from text
    >>> decrypt('113535859035722866')
    'cat'

    :return:
    """
    # Bob picks two large primes p and q
    p, q = 885320963, 238855417
    n = p * q
    e = 9007

    # Bob calculates d
    from basicnumbertheory.cryptomath import findModInverse
    d = findModInverse(e, (p-1)*(q-1))

    # Bob computes c^d(mod n)
    m = str(pow(long(ciphertext), d, n))

    # Convert back to alphabets
    if len(m) % 2:
        m = '0' + m
    plaintext = ''
    for i in range(0, len(m), 2):
        plaintext += chr(int(m[i:i+2]) - 1 + ord('a'))

    return plaintext


def encrypt(message, n, e):
    """
    Example from text
    >>> encrypt("cat", 211463707796206571, 9007)
    '113535859035722866'

    :param message:
    :return:
    """
    # Convert message to integer representation
    m = ''
    for letter in message:
        m += "{0:0>2}".format(ord(letter) - ord('a') + 1)
    m = int(m)

    # Alice encrypts m by using public n and e
    c = pow(m, e, n)
    return str(c)
