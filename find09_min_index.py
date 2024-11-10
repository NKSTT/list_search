def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    a = min(data)
    return data.index(a)
print (find_min_index([12, 2, 5, 2, 7, 9, 1]))
