def block_cipher(text, switch):
    """
    >>> block_cipher('abc', 0)
    'axw'

    >>> block_cipher('cat', 0)
    'dtc'

    >>> block_cipher('op', 0)
    'pye'

    >>> block_cipher('matrix', 0)
    'nngqvx'

    >>> block_cipher('blockcipher', 0)
    'rbzmuepyonom'

    >>> block_cipher('ciphertext', 0)
    'rxscfzcffawp'

    >>> block_cipher('axw', 1)
    'abc'

    >>> block_cipher('dtc', 1)
    'cat'

    >>> block_cipher('pye', 1)
    'opx'

    >>> block_cipher('nngqvx', 1)
    'matrix'

    >>> block_cipher('rbzmuepyonom', 1)
    'blockcipherx'

    >>> block_cipher('rxscfzcffawp', 1)
    'ciphertextxx'

    :param text: text to be encrypted/decrypted
    :return: Encrypted/decrypted text
    """
    import numpy as np
    from basicnumbertheory.inv_matrix_mod import inv_matrix_mod

    # Pick a key
    n = 3
    m = [[1, 2, 3],
         [4, 5, 6],
         [11, 9, 8]]
    m_inv = inv_matrix_mod(m, 26)

    # encrypt or decrypt depending on the key
    if switch:
        key = m_inv
    else:
        key = m

    # Figure out how many times we need to run the algorithm
    length = len(text)
    rounds = length/3

    # Append the plaintext with 'x's otherwise we will not be able to do matrix
    # multiplication
    if length % 3:
        rounds += 1
        text += 'x' * (3 - length % 3)


    c_text = ''
    for i in range(rounds):
        # Create the vector for matrix multiplication
        vector = []
        for letter in text[3 * i: 3 * (i + 1)]:
            vector.append(ord(letter) - ord('a'))

        # Convert the ciphertext from its number representation to characters
        c = np.dot(vector, key) % 26
        for num in c:
            c_text += (chr(num + ord('a')))

    return c_text

