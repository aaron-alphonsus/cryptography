def frequency(text):
    # TODO: change function input to a textfile?
    """
    Takes in text and returns a dict with the count of each character

    :param text:
    :return:
    """
    import collections
    freq = collections.Counter(text)
    print freq
    return freq

# frequency("viginere")

# def printfile(file_name):
#     ifp = open(file_name)
