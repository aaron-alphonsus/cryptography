def inv_matrix_mod(m, n):
    """
    Calculates inverse m (mod n). Uses the numpy library to calculate the
    determinant and adj. matrix.

    Textbook example
    >>> m = [[1, 2],
    ...      [3, 4]]
    >>> inv_matrix_mod(m, 11)
    [[9, 1], [7, 5]]

    Textbook example 3x3
    >>> m = [[1, 1, 1],
    ...      [1, 2, 3],
    ...      [1, 4, 9]]
    >>> inv_matrix_mod(m, 11)
    [[3, 3, 6], [8, 4, 10], [1, 4, 6]]

    Random example
    >>> m = [[4, 7],
    ...      [2, 6]]
    >>> inv_matrix_mod(m, 11)
    [[5, 7], [2, 7]]

    Invalid example
    >>> m = [[4, 7],
    ...      [2, 6]]
    >>> inv_matrix_mod(m, 15)
    []

    :param m: Matrix
    :param n: modulus
    :return: [] if det(m), n are not relatively prime
             m (mod n), otherwise
    """
    import numpy as np
    import cryptomath

    size = len(m)

    # Matrix determinant
    det = int(np.around(np.linalg.det(m)))

    # if gcd(determinant, n) is not 1, return empty matrix
    if not cryptomath.gcd(det, n) == 1:
        return []

    # calculate adj(matrix) and mod inverse of determinant
    m_inv = det * np.linalg.inv(m)
    # print m_inv
    inv = cryptomath.findModInverse(det, n)

    # multiply matrix inverse with mod inverse and take (mod n) to get positive
    # values. Return inv m (mod n)
    for i in range(size):
        for j in range(size):
            m_inv[i][j] = int(np.around(m_inv[i][j] * inv % n))

    m_inv = m_inv.astype(int).tolist()
    return m_inv
