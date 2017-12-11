from simpdes import encrypt, expander, s1_box, s2_box

def diff_cryptanalysis(message, message_star, key):
    """
    >>> diff_cryptanalysis(['000111011011', '010111011011'], \
    ['101110011011', '101110011011'], '010011010')
    None

    :param message:
    :param message_b:
    :param key:
    :return:
    """
    possible_k4_l = []
    possible_k4_r = []
    k4_l = ''
    k4_r = ''
    for i in range(2):
        left1, right1 = message[i][0:6], message[i][6:12]

        output = encrypt(message[i], key, 3)
        left4, right4 = output[0:6], output[6:12]

        # print left1, right1
        # print left4, right4

        left_star1, right_star1 = message_star[i][0:6], message_star[i][6:12]

        output_star = encrypt(message_star[i], key, 3)
        left_star4, right_star4 = output_star[0:6], output_star[6:12]

        # print left_star1, right_star1
        # print left_star4, right_star4

        left_prime1 = "{0:06b}".format(int(left1, 2) ^ int(left_star1, 2))
        right_prime1 = "{0:06b}".format(int(right1, 2) ^ int(right_star1, 2))  # expected because right1 = right_star1
        left_prime4 = "{0:06b}".format(int(left4, 2) ^ int(left_star4, 2))
        right_prime4 = "{0:06b}".format(int(right4, 2) ^ int(right_star4, 2))
        # print left_prime1, right_prime1
        # print left_prime4, right_prime4

        e_left4 = expander(left4)
        # print expander(left_b4)

        e_left_prime4 = expander(left_prime4)
        s1_input, s2_input = e_left_prime4[:4], e_left_prime4[4:]

        sbox_output = "{0:06b}".format(int(right_prime4, 2) ^ int(left_prime1, 2))
        s1_output, s2_output = sbox_output[:3], sbox_output[3:]

        # print s1_input, s2_input
        # print s1_output, s2_output

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

        # print possible_k4_l, possible_k4_r

    k4 = k4_l + k4_r + '*'
    print k4
    k = k4[6:] + k4[:6]
    print k






