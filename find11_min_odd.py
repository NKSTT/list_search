def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    a = [num for num in data if num % 2 != 0]
    x = min(a)
    return x
print (find_min_odd([1, 8, 2, 8, 5]))
print (find_min_odd([7, 8, 4, 3, 5]))