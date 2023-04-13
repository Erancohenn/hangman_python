def choose_word(file_path, index):
    """
    Extract word with a given index from the file.
    :param file_path: path to the file
    :param index: specific word chosen by index
    :type file_path: str
    :type index: int
    :return: Word from the file chosen by index
    :rtype: str
    """

    openfile = open(file_path, "r")
    readfile = openfile.read()
    words = readfile.split(" ")
    no_doubles = []
    for i in words:
        if i not in no_doubles:
            no_doubles.append(i)

    len_no_doubles = len(no_doubles)
    new_index = index % len_no_doubles
    word = no_doubles[new_index-1]
    openfile.close()
    return word

