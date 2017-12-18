
def linear_search(value, x, *args):
    for i, elem in enumerate(x):
        if elem == value:
            return i
    return None


def binary_search(value, x, i, j):
    """ Assumes input x is a sorted list. Returns the index
    i at which x[i] == value, or None if x does not contain value.
    """
    if i > j:
        return None
    n = (i + j) // 2
    if x[n] == value:
        return n
    elif value < x[n]:
        return binary_search(value, x, i, n-1)
    else:
        return binary_search(value, x, n+1, j)


def test_search_algo(search_func):
    assert search_func(2, [1,2,3], 0, 2) == 1
    assert search_func(10, [7,9,10], 0, 2) == 2
    assert search_func(2, [1,3], 0, 1) == None


def test():
    algorithms = [
        linear_search,
        binary_search,
    ]
    for algo in algorithms:
        test_search_algo(algo)


if __name__ == '__main__':
    test()

