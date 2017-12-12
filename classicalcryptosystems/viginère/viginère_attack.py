# Frequency of letters in the English language
FREQUENCY = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070,
             0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060,
             0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]


def viginere_attack():
    """
    This is more of an example than an actual attack. One of the reasons being
    the book isn't very clear about where to stop while finding the key length.

    This algorithm is an implementation of the example they do in the textbook
    to find the key for the piece of text given below
    :return:
    """
    ciphertext = "vvhqwvvrhmusgjgthkihtssejchlsfcbgvwcrlryqtfsvgahwkcuhwauglq" \
                 "hnslrljshbltspisprdxljsveeghlqwkasskuwepwqtwvspgoelkcqyfnsv" \
                 "wljsniqkgnrgybwlwgoviokhkazkqkxzgyhcecmeiujoqkwfwvefqhkijrc" \
                 "lrlkbienqfrjljsdhgrhlsfqtwlauqrhwdmwlgusgikkflryvcwvspgpmlk" \
                 "assjvoqxeggveyggzmljcxxljsvpaivwikvrdrygfrjljslveggveyggeia" \
                 "puuisfpbtgnwwmuczrvtwglrwugumnczvile"


    coincidences = [0]*6
    highest = 0
    key_len = -1
    # Take a displacement of the ciphertext and calculate the number of
    # coincidences each time.
    # Find the highest value and its position. This is your key length
    for displacement in range(1, 7):
        i = 0
        j = displacement
        # j keeps track of the displaced ciphertext while i keeps track of the
        # original
        while j < len(ciphertext):
            if ciphertext[j] == ciphertext[i]:
                coincidences[displacement-1] += 1
            j += 1
            i += 1
        # update highest if new highest found
        if coincidences[displacement-1] > highest:
            highest = coincidences[displacement-1]
            key_len = displacement

    key = ''
    for i in range(key_len):

        v = [0]*26
        w = []
        num = 0
        while i < len(ciphertext):
            # calculate frequency of characters at i, i+key_len, i+2*key_len ...
            # store it in v
            v[ord(ciphertext[i]) - ord('a')] += 1
            i += key_len
            num += 1

        # Divide v by number of characters counted
        for j in range(len(v)):
            w.append(float(v[j])/num)

        highest = 0
        pos = -1
        A = FREQUENCY
        # Calculate the dot product W.A(j) and keep track of the highest value
        # and its position. This position is a letter of the key
        for j in range(26):
            if sum(p * q for p, q in zip(w, A[-j:] + A[:-j])) > highest:
                highest = sum(p * q for p, q in zip(w, A[-j:] + A[:-j]))
                pos = j

        # Add the letter to the key
        key += chr(pos + ord('a'))

    print key


viginere_attack()
