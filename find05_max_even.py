def find_max_even(data):
    """
    Given the list of numbers, find the maximum even number in the list.
    args:
        data: list of numbers
    returns: maximum even number in the list, or None if no even number exists
    """
    a = [b for b in data if b%2 == 0]
    if a:
        return max(a)
    else:
        return None
print (find_max_even([1, 4, 3, 8, 5]))