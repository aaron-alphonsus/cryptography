num_alphabets = 26


def encode(plaintext, k):
    """
    Shifts each letter of the plaintext by the key provided

    Example from the text
    >>> encode('hereishowitworks', (21, 4, 2, 19, 14, 17))
    'citxwjcsybhnjvml'

    Example with upper case characters
    >>> encode('heReishOwitWorkS', (21, 4, 2, 19, 14, 17))
    'ciTxwjcSybhNjvmL'

    :param plaintext: plaintext to be encrypted
    :param k: key vector
    :return: encrypted plaintext
    """
    from itertools import cycle

    ciphertext = ''
    k = cycle(k)             # To iterate through the key in a circular fashion

    # Take away ord('a') to get in the range 0 - 25. From there, add the shift
    # and % 26 to get the right letter between 0 and 25. Now add ord('a') to
    # get the right ascii value and cast to a chr.
    for letter in plaintext:
        # Handles upper case letter transformations
        if ord('A') <= ord(letter) <= ord('Z'):
            ciphertext += chr((ord(letter) - ord('A') + next(k)) %
                              num_alphabets + ord('A'))
        # Handles lower case letter transformations
        elif ord('a') <= ord(letter) <= ord('z'):
            ciphertext += chr((ord(letter) - ord('a') + next(k)) %
                              num_alphabets + ord('a'))

    return ciphertext


def decode(ciphertext, k):
    """
    Shifts each letter of the ciphertext by the key provided

    Example from the text
    >>> decode('citxwjcsybhnjvml', (21, 4, 2, 19, 14, 17))
    'hereishowitworks'

    Example with upper case characters
    >>> decode('ciTxwjcSybhNjvmL', (21, 4, 2, 19, 14, 17))
    'heReishOwitWorkS'

    :param plaintext: ciphertext to be decrypted
    :param k: key vector
    :return: decrypted ciphertext
    """
    from itertools import cycle

    plaintext = ''
    k = cycle(k)             # To iterate through the key in a circular fashion

    # Take away ord('a') to get in the range 0 - 25. From there, take away the
    # shift and % 26 to get the right letter between 0 and 25. Now add ord('a')
    # to get the right ascii value and cast to a chr.
    for letter in ciphertext:
        # Handles upper case letter transformations
        if ord('A') <= ord(letter) <= ord('Z'):
            plaintext += chr((ord(letter) - ord('A') - next(k)) %
                              num_alphabets + ord('A'))
        # Handles lower case letter transformations
        elif ord('a') <= ord(letter) <= ord('z'):
            plaintext += chr((ord(letter) - ord('a') - next(k)) %
                              num_alphabets + ord('a'))

    return plaintext
