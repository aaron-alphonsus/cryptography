def des(plaintext, key):
    """
    Huge thank you to https://billstclair.com/grabbe/des.htm
    Allowed me to see step-by-step output from the DES which made doctesting
    really simple and effective

    >>> des('8787878787878787', '0E329232EA6D0D73')
    '0'
    >>> des('0123456789ABCDEF', '133457799BBCDFF1')
    '85e813540f0ab405'

    :param plaintext:
    :param key:
    :return:
    """

    # print format(bin(int(plaintext, 16)), '#64b')
    m = bin(int(plaintext, 16))[2:].zfill(64)
    # print m

    # key has 56 bits -> expressed as a 64-bit string (parity bits after every
    #   8 bits) (Comes into play later)
    k = bin(int(key, 16))[2:].zfill(64)
    c, d = key_permutation(k)
    # print k

    left, right = initial_permutation(m)

    for i in range(1, 17):
        prev_left = left

        # Calculate new key
        c, d = left_shift(c, d, i)
        k = cd_pick(c, d)

        left = right
        right = "{0:032b}".format(int(prev_left, 2) ^ int(f(right, k), 2))

    c = inverse_ip(right+left)
    return "%x" % int(c, 2)


def initial_permutation(m):
    """
    The initial message is run through  a permutation function

    >>> initial_permutation('0000000100100011010001010110011110001001101010111100110111101111')
    ('11001100000000001100110011111111', '11110000101010101111000010101010')

    :param m: The initial message to be permuted
    :return: The left and right values that make up the permuted message
    """
    m0 = ''
    ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54,
          46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33,
          25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21,
          13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    for i in ip:
        m0 += m[i - 1]

    left0, right0 = m0[:32], m0[32:]
    return left0, right0


def key_permutation(k):
    """
    The key runs through a permutation which also serves to discard of the
     parity bits.

    >>> key_permutation('0001001100110100010101110111100110011011101111001101111111110001')
    ('1111000011001100101010101111', '0101010101100110011110001111')

    :param k: The original 64-bit key
    :return: 56-bit key with parity bits discarded
    """
    k0 = ''
    kp = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
          10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
          63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
          14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    for i in kp:
        k0 += k[i - 1]

    c0, d0 = k0[:28], k0[28:]
    return c0, d0


def left_shift(c, d, i):
    """
    Depending on which round, the left and right 28 bits of the key are shifted
    to the left

    >>> left_shift('1111000011001100101010101111', '0101010101100110011110001111', 1)
    ('1110000110011001010101011111', '1010101011001100111100011110')

    >>> left_shift('1100001100110010101010111111', '0101010110011001111000111101', 3)
    ('0000110011001010101011111111', '0101011001100111100011110101')

    :param c: Left 28 bits of key
    :param d: Right 28 bits of key
    :param i: Iteration
    :return: c, d shifted by appropriate value
    """
    ls = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    return c[ls[i-1]:] + c[:ls[i-1]], d[ls[i-1]:] + d[:ls[i-1]]


def cd_pick(c, d):
    """
    This algorithm chooses 48 bits from the 56 bit string. This 48-bit key then
    gets XORed with the permuted key

    >>> cd_pick('1110000110011001010101011111', '1010101011001100111100011110')
    '000110110000001011101111111111000111000001110010'

    :param c: Left 28 bits of key
    :param d: Right 28 bits of key
    :return: Key for iteration i
    """
    k = c + d
    ki = ''
    cd = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
          23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
          41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
          44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    for i in cd:
        ki += k[i-1]

    return ki


def f(r, k):
    """
    Once again, like in simpdes, f is one of the main, if not the main functions.
    It takes in the right 32 bits of the message and the key
    It calls the expansion function, produces the inputs for the s-boxes and
    gets the outputs, finally calling a function to permute the returned string

    >>> f('11110000101010101111000010101010', '000110110000001011101111111111000111000001110010')
    '00100011010010101010100110111011'

    :param r: Right 32 bits of the message
    :param k: The permuted key
    :return: 32-bit intermediate ciphertext
    """
    er = expansion(r)

    bj = "{0:048b}".format(int(er, 2) ^ int(k, 2))
    b = []
    for i in range(1, 9):
        b.append(bj[6*(i-1):6*i])

    c = s_boxes(b)
    c = ''.join(c)
    return permute_string(c)


def expansion(r):
    """
    Expands the r value to XOR with the 48 bit permuted key

    >>> expansion('11110000101010101111000010101010')
    '011110100001010101010101011110100001010101010101'

    :param r: 32-bit value to be expanded to 48 bits
    :return: 48-bit expanded value
    """
    er = ''
    ep = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
          8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
          24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    for i in ep:
        er += r[i - 1]

    return er


def s_boxes(b):
    """
    Takes in the inputs and indexes the S-boxes to produce the outputs

    >>> s_boxes(['011000', '010001', '011110', '111010', '100001', '100110', '010100', '100111'])
    ['0101', '1100', '1000', '0010', '1011', '0101', '1001', '0111']

    :param b: List containing inputs b1, b2, ..., b8
    :return: List containing outputs c1, c2, ..., c8
    """
    s = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    i = 0
    c = []
    for bits in b:
        # Caluclate the row and column to reference the S-boxes and get the
        # output
        row = int(bits[0]+bits[5], 2)
        col = int(bits[1:5], 2)
        c.append("{0:04b}".format(s[i][row][col]))
        i += 1
    return c


def permute_string(c):
    """
    Run the string received from the s-boxes in a permutation

    >>> permute_string('01011100100000101011010110010111')
    '00100011010010101010100110111011'

    :param c: c string to be permuted
    :return: permuted 32-bit string
    """
    c0 = ''
    cp = [16, 7, 20, 21, 29, 12, 28, 17, 1,  15, 23, 26, 5,  18, 31, 10,
          2,  8, 24, 14, 32, 27, 3,  9,  19, 13, 30, 6,  22, 11, 4,  25]
    for i in cp:
        c0 += c[i - 1]

    return c0


def inverse_ip(r16l16):
    """
    Run the final left and right values (switched) on the inverse of the initial
    permutation to get the ciphertext

    >>> inverse_ip('0000101001001100110110011001010101000011010000100011001000110100')
    '1000010111101000000100110101010000001111000010101011010000000101'

    :param r16l16: The final permutation r16l16
    :return: Permutation of the string to yield the ciphertext
    """
    c = ''
    inv_ip = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41,  9, 49, 17, 57, 25]
    for i in inv_ip:
        c += r16l16[i - 1]

    return c