def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first = list(first_string.lower())
    second = list(second_string.lower())

    for elem in first:
        if elem in second:
            return second.remove(elem)
        return False

    return len(second) == 0
