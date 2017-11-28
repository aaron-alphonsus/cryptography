# TODO: Moar doctest/unittests!
# TODO: Different representation of message for more plaintext values?


def decrypt(cipher):
    """
    Takes in the cipher and decrypts it using the private value d and public
    value n in the formula c^d(mod n). Converts this decrypted string back to
    its alphabetical values

    Example from text
    >>> decrypt('76361619689947957826453014003338795527690911871909025105191' \
    '14360407469817440544361685224233679312049978294736018243999366707605193' \
    '77943012567374518731052479394802774791886382977743888869194550652445100' \
    '81814714844755050106261709278066809724007140851120259132888147550135672' \
    '854933871225677514975441223538079138')
    'cat'

    :return: Decrypted cipher
    """
    setup()

    # Read in p, q, and d from the private key file
    ifp = open("private.rsa")
    private = ifp.readlines()
    d = int(private[-1])

    # Read in n from the public key file
    ifp = open("public.rsa")
    public = ifp.readlines()
    n = int(public[-1])

    # Compute c^d(mod n)
    m = str(pow(long(cipher), d, n))

    # Convert back to alphabets
    if len(m) % 2:
        m = '0' + m
    plaintext = ''
    for i in range(0, len(m), 2):
        plaintext += chr(int(m[i:i+2]) - 1 + ord('a'))

    return plaintext


def encrypt(message):
    """
    This is an implementation from the text. Assumes all messages to be
    encrypted will be strings of all lowercase letters. It takes the message
    and converts it to its integer representation, then encrypts it using the
    formula m^e(mod n)

    Example from text
    >>> encrypt("cat")
    '76361619689947957826453014003338795527690911871909025105191143604074698174405443616852242336793120499782947360182439993667076051937794301256737451873105247939480277479188638297774388886919455065244510081814714844755050106261709278066809724007140851120259132888147550135672854933871225677514975441223538079138'

    :param message: The message to be encrypted
    :return: Encrypted plaintext
    """
    setup()

    # Convert message to integer representation
    m = ''
    for letter in message:
        m += "{0:0>2}".format(ord(letter) - ord('a') + 1)
    m = int(m)

    # Read in e and n from the public key file
    ifp = open("public.rsa")
    e, n = int(ifp.readline()), int(ifp.readline())

    # Encrypt m by using public n and e
    c = pow(m, e, n)
    return str(c)


def setup():
    """
    Helper function to add d to the private rsa file and n to the public rsa
    file.
    :return: None
    """
    # Check if d has been printed in private.rsa
    # (if d is missing, n assumed missing)
    ifp = open("private.rsa")
    num_lines = sum(1 for line in ifp)
    ifp.close()

    if num_lines == 2:
        ifp = open("private.rsa")
        p, q = int(ifp.readline()), int(ifp.readline())

        ifp = open("public.rsa")
        e = int(ifp.readline())

        # Append d to the private file
        ofp = open("private.rsa", "a")
        from basicnumbertheory.cryptomath import findModInverse
        ofp.write("\n" + str(findModInverse(e, (p - 1) * (q - 1))))

        # Append n to the private file
        ofp = open("public.rsa", "a")
        ofp.write("\n" + str(p * q))
