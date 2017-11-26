# TODO: Decryption
# TODO: Extend to actual character en/de-cryption


def encrypt(message, key, rounds=4):
    """
    Takes in a 12-bit message and splits it into two 6-bit messages left(0) and
    right(0).
    The algorithm is calculated as follows (for 'i' = 1 to 'rounds'):
    left(i) = right(i-1)
    right(i) = left(i-1) xor f(right(i-1), key(i))
    
    Example from text
    >>> encrypt('011100100110', '011001010', 1)
    '100110011000'
    
    Testing 4 rounds
    >>> encrypt('011100100110', '011001010')
    '001100010110'

    :param message: 12-bit message to be encrypted
    :param key: 9-bit key
    :param rounds: Number of rounds - defaults to 4
    :return: Encrypted message
    """
    left, right = message[0:6], message[6:12]
    for i in range(1, rounds+1):
        prev_l = left

        # Calculate new key
        s = (i-1) % 9
        e = (i-1) % 9 + 8
        o = 8 - (min(e,9) - s)
        k = key[s:e] + key[:o]

        # Calculate new left and right
        left = right
        right = int(prev_l, 2) ^ int(f(right, k), 2)
        right = "{0:06b}".format(right)

    return left + right


def f(r, key):
    """
    The f function takes in an r value

    >>> f('100110', '01100101')
    '000100'

    :param r: 6-bit previous right
    :param key: 8-bit current key
    :return: 6-bit output from the 2 S-boxes
    """
    key = int(key, 2)
    result = int(expander(r), 2)
    result ^= key
    result = "{0:08b}".format(result)

    return s_boxes(result[0:4], result[4:8])


def expander(r):
    """
    This function takes a 6-bit input and produces an 8-bit output.
    Numbering the input bits 1, 2, 3, 4, 5, 6 the output bits will be:
    1, 2, 4, 3, 4, 3, 5, 6

    >>> expander('011001')
    '01010101'

    :param r: 6-bit string
    :return: Input expanded to 8-bit string
    """
    return r[0] + r[1] + r[3] + r[2] + r[3] + r[2] + r[4] + r[5]


def s_boxes(input1, input2):
    """
    Uses input1 and input2 to index into the two S-boxes

    :param input1: First 4 bits of (expander(r) xor key)
    :param input2: Last 4 bits of (expander(r) xor key)
    :return: 6-bit concatenated S-box output
    """
    s1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
          ['001', '100', '110', '010', '000', '111', '101', '011']]
    r1, c1 = int(input1[0]), int(input1[1:4], 2)

    s2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
          ['101', '011', '000', '111', '110', '010', '001', '100']]
    r2, c2 = int(input2[0]), int(input2[1:4], 2)

    return s1[r1][c1] + s2[r2][c2]
