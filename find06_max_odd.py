def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a = [num for num in data if num%2 != 0]
    if a:
        return max(a)
    else:
        return -1

print (find_max_odd([11, 7, 5, 4, 9]))
print (find_max_odd([14, 2, 4, 4, 6]))