def encode(plaintext, alpha, beta, num_alphabets):
    """
    The encode function works on the input string, transforming each letter by
    multiplying it by alpha and adding beta to it. It handles both uppercase
    and lowercase inputs.
    Command Line Example:
        python -c 'from affine import encode; print encode("affine", 9, 2)'

    Examples from the text
    >>> encode('affine', 9, 2, 26)
    'cvvwpm'
    >>> encode('input', 13, 4, 26)
    Ciphertext will not have a unique decryption.
    gcd(13, 26) does not equal 1.

    Example with upper case characters
    >>> encode('AFfiNe', 9, 2, 26)
    'CVvwPm'

    :param plaintext: plaintext to be encrypted
    :param alpha: alpha coefficient for the affine cipher
    :param beta: beta coefficient for the affine cipher
    :param num_alphabets: characters used in our encryption
    :return: encrypted plaintext
    """
    from fractions import gcd
    if gcd(alpha, num_alphabets) is not 1:
        print "Ciphertext will not have a unique decryption."
        print "gcd(" + str(alpha) + ", " + str(num_alphabets) + ") does not " \
                                                                "equal 1."
        return

    cipher_text = ''

    for letter in plaintext:
        # Handles upper case letter transformations
        if ord('A') <= ord(letter) <= ord('Z'):
            cipher_text += chr((alpha * (ord(letter)-ord('A')) + beta) %
                               num_alphabets + ord('A'))
        # Handles lower case letter transformations
        elif ord('a') <= ord(letter) <= ord('z'):
            cipher_text += chr((alpha * (ord(letter)-ord('a')) + beta) %
                               num_alphabets + ord('a'))

    return cipher_text


def decode(cipher_text, alpha, beta, num_alphabets):
    """
    decode calculates the decryption function (if possible) and then decrypts
    the string.

    Examples from the text
    >>> decode('cvvwpm', 9, 2, 26)
    'affine'
    >>> decode('errer', 13, 4, 26)
    Ciphertext does not have a unique decryption.
    gcd(13, 26) does not equal 1.

    Example with upper case characters
    >>> decode('CVvwPm', 9, 2, 26)
    'AFfiNe'

    :param cipher_text: ciphertext to be decrypted
    :param alpha: alpha coefficient for the affine cipher
    :param beta: beta coefficient for the affine cipher
    :param num_alphabets: characters used in our encryption
    :return: decrypted ciphertext
    """
    # Adding folder containing cryptomath module to the path
    import os
    import sys

    os.chdir('..')
    sys.path.insert(1, os.path.join(os.getcwd(), 'basicnumbertheory'))
    from basicnumbertheory.cryptomath import findModInverse

    # Finding decryption function (if possible) and decrypting ciphertext
    alpha_inv = findModInverse(alpha, num_alphabets)
    if alpha_inv == -1:
        print "Ciphertext does not have a unique decryption."
        print "gcd(" + str(alpha) + ", " + str(num_alphabets) + ") does not " \
                                                                "equal 1."
        return

    plaintext = ''

    for letter in cipher_text:
        # Handles upper case letter transformations
        if ord('A') <= ord(letter) <= ord('Z'):
            plaintext += chr((alpha_inv * (ord(letter) - ord('A') - beta)) %
                             num_alphabets + ord('A'))
        # Handles lower case letter transformations
        elif ord('a') <= ord(letter) <= ord('z'):
            plaintext += chr((alpha_inv * (ord(letter) - ord('a') - beta)) %
                             num_alphabets + ord('a'))

    return plaintext
