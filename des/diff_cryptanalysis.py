from simpdes import encrypt, expander, s1_box, s2_box


def diff_cryptanalysis(message, message_star, key):
    """
    Differential cryptanalysis is a chosen plaintext attack on the DES. By
    comparing the differences in the produced ciphertext, we can deduce
    information about the key used.

    >>> diff_cryptanalysis(['000111011011', '010111011011'], \
    ['101110011011', '101110011011'], '010011010')
    '001001101'

    :param message: The two plaintexts to be encrypted
    :param message_star: The suitbly chosen 'paired' plaintexts
    :param key: The key that we want to deduce
    :return: The key that we have deciphered
    """
    possible_k4_l = []
    possible_k4_r = []
    k4_l = ''
    k4_r = ''
    for i in range(2):
        # Split the chosen plaintext into left and right
        left1, right1 = message[i][0:6], message[i][6:12]

        # Run the message on the 3 round simpdes
        output = encrypt(message[i], key, 3)
        left4, right4 = output[0:6], output[6:12]

        # This is the chosen plaintext pair
        left_star1, right_star1 = message_star[i][0:6], message_star[i][6:12]

        # Run the pair through simpdes
        output_star = encrypt(message_star[i], key, 3)
        left_star4, right_star4 = output_star[0:6], output_star[6:12]

        # The primes are calculated as the difference between the plaintext pair
        # XOR yields the required result
        left_prime1 = "{0:06b}".format(int(left1, 2) ^ int(left_star1, 2))
        right_prime1 = "{0:06b}".format(int(right1, 2) ^ int(right_star1, 2))
        left_prime4 = "{0:06b}".format(int(left4, 2) ^ int(left_star4, 2))
        right_prime4 = "{0:06b}".format(int(right4, 2) ^ int(right_star4, 2))

        e_left4 = expander(left4)

        # Calculates the XOR input and output for the s-boxes
        e_left_prime4 = expander(left_prime4)
        s1_input, s2_input = e_left_prime4[:4], e_left_prime4[4:]

        sbox_output = "{0:06b}".format(int(right_prime4, 2) ^ int(left_prime1, 2))
        s1_output, s2_output = sbox_output[:3], sbox_output[3:]

        # Find and append the s-box pairs that work
        p1 = []
        p2 = []
        for j in range(pow(2, 4)):
            num1, num2 = "{0:04b}".format(int(s1_input, 2) ^ j), "{0:04b}".format(j)
            if int(s1_output, 2) == int(s1_box(num1), 2) ^ int(s1_box(num2), 2):
                p1.append((num1, num2))

            num3, num4 = "{0:04b}".format(int(s2_input, 2) ^ j), "{0:04b}".format(j)
            if int(s2_output, 2) == int(s2_box(num3), 2) ^ int(s2_box(num4), 2):
                p2.append((num3, num4))

        # Add possible first 4 bits of k4
        bits1 = "{0:04b}".format(int(p1[0][0], 2) ^ int(e_left4[:4], 2))
        bits2 = "{0:04b}".format(int(p1[0][1], 2) ^ int(e_left4[:4], 2))
        if bits1 in possible_k4_l:
            k4_l = bits1
        else:
            possible_k4_l.append(bits1)
        if bits2 in possible_k4_l:
            k4_l = bits2
        else:
            possible_k4_l.append(bits2)


        # Add possible 'last' 4 bits of k4 (The last element of the 9-bit key is
        # unknown at this time)
        bits1 = "{0:04b}".format(int(p2[0][0], 2) ^ int(e_left4[4:], 2))
        bits2 = "{0:04b}".format(int(p2[0][1], 2) ^ int(e_left4[4:], 2))
        if bits1 in possible_k4_r:
            k4_r = bits1
        else:
            possible_k4_r.append(bits1)
        if bits2 in possible_k4_r:
            k4_r = bits2
        else:
            possible_k4_r.append(bits2)

    # Append l, r and unknown last character to create k4
    k4 = k4_l + k4_r + '*'
    k2 = k4[7:] + k4[:7]           # Create k2 NOT k1. k1 encrypts l0r0 NOT l1r1

    # Make 2 keys: one where you replace * with 0, and the other where you
    # replace it with 1
    k_i = k2.replace('*', '0')
    k_j = k2.replace('*', '1')

    l4r4 = encrypt(message[0], key, 3)

    if l4r4 == encrypt(message[0], k_i, 3):
        return k_i[8:] + k_i[:8]                 # Convert the key from k2 to k1

    if l4r4 == encrypt(message[0], k_j, 3):
        return k_j[8:] + k_j[:8]                 # Convert the key from k2 to k1
