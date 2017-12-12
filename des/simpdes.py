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

    Testing 3 rounds from textbook example for diff cryptanalysis
    >>> encrypt('000111011011', '010011010', 3)
    '000011100101'

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
        start = (i - 1) % 9
        end = (i - 1) % 9 + 8
        overflow = 8 - (min(end, 9) - start)
        k = key[start:end] + key[:overflow]

        # Calculate new left and right
        left = right
        right = int(prev_l, 2) ^ int(f(right, k), 2)
        right = "{0:06b}".format(right)
        # print left, right, k

    return left + right


def decrypt(ciphertext, key, rounds=4):
    """
    Takes in a 12-bit ciphertext and splits it into two 6-bit ciphertexts
    left(0) and right(0).
    The algorithm is calculated as follows (for 'rounds' to 0, decrementing):
    right(i-1) = left(i)
    left(i-1) = right(i) xor f(left(i), key(i))

    Example from text
    >>> decrypt('100110011000', '011001010', 1)
    '011100100110'

    Testing 4 rounds
    >>> decrypt('001100010110', '011001010')
    '011100100110'

    :param ciphertext: 12-bit ciphertext to be decrypted
    :param key: 9-bit key
    :param rounds: Number of rounds - defaults to 4
    :return: Decrypted ciphertext
    """
    left, right = ciphertext[0:6], ciphertext[6:12]
    for i in range(rounds, 0, -1):
        next_r = right

        # Calculate new key
        start = (i - 1) % 9
        end = (i - 1) % 9 + 8
        overflow = 8 - (min(end, 9) - start)
        k = key[start:end] + key[:overflow]

        # Calculate new left and right
        right = left
        left = int(next_r, 2) ^ int(f(left, k), 2)
        left = "{0:06b}".format(left)

    return left + right


def f(r, key):
    """
    The f function is a large part of the DES and calls a lot of other functions
    Takes in an r value and expands it.
    Takes an XOR of the key and result, formatting the result to 8 bits
    First 4 bits go to S1 and last 4 go to S2. They each return a 3-bit output
    which is concatenated to form a 6-bit result.

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

    TODO: split into two functions s1 and s2 to make diff cryptanalysis easy

    :param input1: First 4 bits of (expander(r) xor key)
    :param input2: Last 4 bits of (expander(r) xor key)
    :return: 6-bit concatenated S-box output
    """
    return s1_box(input1) + s2_box(input2)


def s1_box(s1_input):
    s1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
          ['001', '100', '110', '010', '000', '111', '101', '011']]
    r1, c1 = int(s1_input[0]), int(s1_input[1:4], 2)
    return s1[r1][c1]


def s2_box(s2_input):
    s2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
          ['101', '011', '000', '111', '110', '010', '001', '100']]
    r2, c2 = int(s2_input[0]), int(s2_input[1:4], 2)
    return s2[r2][c2]

