# TODO: Documentation of functions
# TODO: Test more rounds
# TODO: Decryption


def simpdes(message, key, rounds = 4):
    """
    >>> simpdes('011100100110', '011001010', 1)
    '100110011000'

    :param message:
    :param key:
    :param rounds:
    :return:
    """
    l, r = message[0:6], message[6:12]
    for i in range(1, rounds+1):
        prev_l = l

        # Calculate new key
        s = (i-1) % 9
        e = (i-1) % 9 + 8
        o = 8 - (min(e,9) - s)
        k = key[s:e] + key[:o]

        # Calculate new l and r
        l = r
        r = int(prev_l, 2) ^ int(f(r, k), 2)
        r = "{0:06b}".format(r)

    return l + r


def f(r, key):
    """
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
    >>> expander('011001')
    '01010101'

    :param r: 6-bit string
    :return: 'Expands' input to 8-bit string
    """
    return r[0] + r[1] + r[3] + r[2] + r[3] + r[2] + r[4] + r[5]


def s_boxes(input1, input2):
    s1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
          ['001', '100', '110', '010', '000', '111', '101', '011']]
    r1, c1 = int(input1[0]), int(input1[1:4], 2)

    s2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
          ['101', '011', '000', '111', '110', '010', '001', '100']]
    r2, c2 = int(input2[0]), int(input2[1:4], 2)

    return s1[r1][c1] + s2[r2][c2]
